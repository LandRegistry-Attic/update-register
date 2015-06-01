from application import app
import json
from flask import request

SUBJECT = {
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


# @app.route('/entry', methods=["GET", "POST", "PUT", "DELETE"])
# def amend_entry():
#     if request.method == 'GET':
#         return 'get called on entry route'
#
#     if request.method == 'POST':
#
#         entry_group_id = request.get_json()["group_id"]
#         entry_category = request.get_json()["category"]
#
#         return json.dumps(get_title('ff'))


#curl -X POST -d '{"a":"1"}' -H "Content-Type: application/json" http://localhost:5003/titles/dn100/groups/1/entries/1
# amend an individual entry
@app.route('/titles/<title_number>/groups/<int:group_position>/entries/<int:entry_position>', methods=["POST"])
def amend_an_entry(title_number, group_position, entry_position):

    title_json = get_title_from_working_register(title_number)

    # change the title according to the posted entry update

    #WRITES THE ENTRY AS UNICODE ATM.

    new_entry = request.get_json()

    title_json["groups"][group_position]["entries"][entry_position] = new_entry

    update_title_on_working_register(title_json)

    return 'wip amend', 200


# insert a new entry
@app.route('/titles/<title_number>/groups/<int:group_position>/entries/<int:entry_position>', methods=["PUT"])
def add_an_entry(title_number, group_position, entry_position):
    return 'wip insert', 201


# delete an entry
@app.route('/titles/<title_number>/groups/<int:group_position>/entries/<int:entry_position>', methods=["DELETE"])
def delete_an_entry(title_number, group_position, entry_position):
    return 'wip delete', 200


# amend a group of entries
@app.route('/titles/<title_number>/groups/<int:group_position>/entries/', methods=["POST"])
def amend_entry_group(title_number, group_position):
    return 'wip group amend', 200


#gets the title from the working register.
def get_title_from_working_register(title_number):
    return SUBJECT


#Updates the register with the amendment
def update_title_on_working_register(title_json):
    app.logger.info(title_json)
    return 'updated'
