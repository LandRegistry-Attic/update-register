from application.models import WorkingTitles
from application import app
from application import db
import json
import yaml
from flask import request


def get_title():
    return {
        "description": "test data",
        "application_reference": "testabr",
        "title_number": "tt12345",
        "dlr": "a dlr",
        "groups": [
            {
                "group_id": "1",
                "category": "ABCD",
                "entries": [
                    {
                        "entry_id": "998",
                        "full_text": "foo"
                    },
                    {
                        "entry_id": "999",
                        "full_text": "bar"
                    }
                ]
            },
            {
                "group_id": "2",
                "category": "EFGH",
                "entries": [
                    {
                        "entry_id": "999",
                        "full_text": "cat"
                    },
                    {
                        "entry_id": "998",
                        "full_text": "mat"
                    }
                ]
            }
        ]
    }


@app.route('/health')
def index():
    return 'update-register running'

# This will start a new version of the register for amendment.  Right now it just adds test data to
# the working register database
@app.route('/start', methods=["POST"])
def start():
    payload = request.get_json()
    title_number = payload["title_number"]
    application_reference = payload["application_reference"]

    title_json = get_title()  # get data as hardcoded string for now
    title_json["title_number"] = title_number  # re-assign payloads title number and abr
    title_json["application_reference"] = application_reference


    write_to_working_titles_database(title_json)
    return 'started title number %s application reference %s' % (title_number, application_reference), 201


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


# insert a group
@app.route('/titles/<title_number>/groups', methods=["PUT"])
def insert_group(title_number):
    title_json = get_title_from_working_register(title_number)

    # Insert to title_json with the payload (a group).  Use PyYAML to convert payload from unicode to ASCII.
    new_group_string = json.dumps(request.get_json())
    new_group_dict = yaml.safe_load(new_group_string)
    title_json["groups"].append(new_group_dict)
    group_position = len(title_json["groups"]) - 1

    update_title_on_working_register(title_json)
    return 'Insert made at group position %i' % group_position, 201


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
def get_title_from_working_register(title_number):
    # Gets the version of title number with the latest ID on the table
    title = None
    sql_text = "SELECT * FROM records WHERE record ->> 'title_number' = '%s' order by id desc limit 1;" % title_number
    result = db.engine.execute(sql_text)
    for row in result:
        title = row['record']
    return title


#Updates the register with the amendment
def update_title_on_working_register(title_json):
    app.logger.info(title_json)
    write_to_working_titles_database(title_json)
    return 'updated'


def write_to_working_titles_database(title_json):
    working_titles_object = WorkingTitles(title_json)
    try:
        db.session.add(working_titles_object)
        db.session.flush()
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
