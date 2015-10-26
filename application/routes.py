from application.models import WorkingTitles
from application import app
from application import db
import json
import yaml
import re
import requests
from flask import request, Response
from sqlalchemy.sql import text
from .utils import convert_register_format

@app.route('/health')
def index():
    return 'update-register running'

# get whole working register
@app.route('/titles/<title_number>', methods=["GET"])
def get_whole_working_register(title_number):
    register_format = request.args.get("format")
    title_json = get_title_from_working_register(title_number, register_format)

    if title_json is not None:
        return json.dumps(title_json, sort_keys=True,
                      indent=4, separators=(',', ': ')), 200
    else:
        return "title not found", 404

# add whole working register
@app.route('/titles', methods=["POST"])
def add_whole_working_register():
    title_json = request.get_json()
    title_exists = check_title_exists(title_json["title_number"])

    if title_exists == True:
        return "Title already exists in DB", 200
    else:
        write_to_working_titles_database(title_json)
        return "Title added", 200


# amend an individual entry
@app.route('/titles/<title_number>/groups/<int:group_position>/entries/<int:entry_position>', methods=["POST"])
def amend_an_entry(title_number, group_position, entry_position):
    title_json = get_title_from_working_register(title_number)

    # Amend title_json with the payload (an entry).  Use PyYAML to convert payload from unicode to ASCII.
    new_entry_string = json.dumps(request.get_json())
    new_entry_dict = yaml.safe_load(new_entry_string)
    title_json["groups"][group_position]["entries"][entry_position] = new_entry_dict

    update_title_on_working_register(title_json)
    return 'amendment made at group position %i, entry position %i' % (group_position, entry_position), 200


# insert a new entry
@app.route('/titles/<title_number>/groups/<int:group_position>/entries', methods=["PUT"])
def insert_entry(title_number, group_position):
    title_json = get_title_from_working_register(title_number)

    # Insert to title_json with the payload (an entry).  Use PyYAML to convert payload from unicode to ASCII.
    new_entry_string = json.dumps(request.get_json())
    new_entry_dict = yaml.safe_load(new_entry_string)
    title_json["groups"][group_position]["entries"].append(new_entry_dict)
    entry_position = len(title_json["groups"][group_position]["entries"]) - 1

    update_title_on_working_register(title_json)
    return 'Insert made at group position %i, entry position %i' % (group_position, entry_position), 201


# delete an entry
@app.route('/titles/<title_number>/groups/<int:group_position>/entries/<int:entry_position>', methods=["DELETE"])
def delete_entry(title_number, group_position, entry_position):
    title_json = get_title_from_working_register(title_number)

    title_json["groups"][group_position]["entries"].pop(entry_position)

    update_title_on_working_register(title_json)
    return 'Delete at group position %i, entry position %i' % (group_position, entry_position), 200

# get the entry structure
@app.route('/entrystructure', methods=["GET"])
def get_entry_structure():
    return json.dumps({"category": "","entry_date": "","entry_id": "","full_text": "","infills": [],"language":"","role_code": "","sequence_number":"","status":"","sub_register":"","template_text": ""})

# insert a group
@app.route('/titles/<title_number>/groups', methods=["PUT"])
def insert_group(title_number):
    title_json = get_title_from_working_register(title_number)

    if title_json:
        # Insert to title_json with the payload (a group).  Use PyYAML to convert payload from unicode to ASCII.
        new_group_string = json.dumps(request.get_json())
        new_group_dict = yaml.safe_load(new_group_string)

        entries = new_group_dict["entries"]

        for entry in entries:
            template_text = entry["template_text"]
            full_text = re.sub('\*CP\*', get_text_for_infill("charge parties", entry["infills"]), template_text)
            full_text = re.sub('\*CD\*', get_text_for_infill("charge date", entry["infills"]), full_text)
            full_text = re.sub('\*O<>O\*', get_text_for_infill("optional", entry["infills"]), full_text)
            #Remove double spaces because of empty option infills
            full_text = re.sub('  ', ' ', full_text)
            entry["full_text"] = full_text

        title_json["groups"].append(new_group_dict)
        group_position = len(title_json["groups"]) - 1

        update_title_on_working_register(title_json)
        return 'Insert made at group position %i' % group_position, 201
    else:
        return 'No title found for {0}'.format(title_number), 500

#get something to complete
@app.route('/complete', methods=["POST"])
def complete():
    header = {"Content-Type":"application/json"}
    req_json = json.loads(request.get_json())
    working_register =  get_title_from_working_register(str(req_json['title_number']))
    req_json['register_details'] = working_register
    data = json.dumps(req_json)

    response = requests.post("http://localhost:8888/RegisterAdapter/complete", data=data , headers=header)
    if response.status_code == requests.codes.ok:
        delete_title_on_working_register(str(req_json['title_number']))

    response.raise_for_status()
    return json.dumps(response.json())


# delete a group
@app.route('/titles/<title_number>/groups/<int:group_position>', methods=["DELETE"])
def delete_a_group(title_number, group_position):
    title_json = get_title_from_working_register(title_number)

    title_json["groups"].pop(group_position)

    update_title_on_working_register(title_json)
    return 'Delete at group position %i' % group_position, 200


# Amend a group
@app.route('/titles/<title_number>/groups/<int:group_position>', methods=["POST"])
def amend_group(title_number, group_position):
    title_json = get_title_from_working_register(title_number)

    # Amend title_json with the payload (entries).  Use PyYAML to convert payload from unicode to ASCII.
    new_group_string = json.dumps(request.get_json())
    new_group_dict = yaml.safe_load(new_group_string)
    title_json["groups"][group_position] = new_group_dict

    update_title_on_working_register(title_json)
    return 'Group amended at group position %i' % group_position, 200


#gets the title from the working register.
def get_title_from_working_register(title_number, register_format=None):
    # Gets the version of title number with the latest ID on the table
    title = None

    if check_title_exists(title_number):
        sql_text = "SELECT * FROM records WHERE record ->> 'title_number' = '%s' order by id desc limit 1;" % title_number
        result = db.engine.execute(sql_text)
        for row in result:
            title = row['record']
    else:
        response = requests.get(app.config['CURRENT_REGISTER_API']+'/register/'+title_number, headers={"Content-Type":"application/json"})
        if response.status_code == 200:
            title = response.json()
            write_to_working_titles_database(title)

    if register_format:
        title = convert_register_format(title, register_format)

    return title


#Updates the register with the amendment
def update_title_on_working_register(title_json):
    # Gets the version of title number with the latest ID on the table
    sql_text = text("UPDATE records SET record = '{0}' WHERE record ->> 'title_number' = '{1}';".format(json.dumps(title_json), title_json["title_number"]))
    result = db.engine.execute(sql_text)

    return 'updated'

#Deletes the title register
def delete_title_on_working_register(title_no):
    sql_text = text("DELETE FROM records WHERE record ->> 'title_number' = '{0}';".format(title_no))
    result = db.engine.execute(sql_text)

    return 'deleted'


def write_to_working_titles_database(title_json):
    working_titles_object = WorkingTitles(title_json)
    try:
        db.session.add(working_titles_object)
        db.session.flush()
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise

def get_text_for_infill(type, infills):
    text = ""
    for infill in infills:
        if (infill["type"] == type) and ("text" in infill):
            text = infill["text"]
    return text

def check_title_exists(title_number):
    # Gets the version of title number with the latest ID on the table
    title_exists = False

    sql_text = "SELECT 1 FROM records WHERE coalesce( case when (record ->> 'title_number') is NULL then null " \
               "else (record ->> 'title_number' = '%s'" % title_number + ") " \
               "end) " \
               "order by id desc limit 1"

    result = db.engine.execute(sql_text)
    for row in result:
        title_exists = True
    return title_exists
