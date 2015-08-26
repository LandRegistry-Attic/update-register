import unittest
import json
import mock
import responses
from flask import Response

from application import app
from application.models import WorkingTitles
from test_data import TITLE_WITH_AMENDED_ENTRY, ENTRY_AMENDMENT, ENTRY_INSERT, TITLE_WITH_INSERTED_ENTRY
from test_data import TITLE_WITH_DELETED_ENTRY, get_target_json, GROUP_INSERT, TITLE_WITH_DELETED_GROUP
from test_data import TITLE_WITH_INSERTED_EMPTY_GROUP, TITLE_WITH_REPLACED_GROUP, GROUP_REPLACE, TEST_REGISTER, TEST_REGISTER2

class TestCaseListView(unittest.TestCase):

    mock_title = {}

    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()
        self.mock_title.clear()


    def test_service_health(self):
        response = self.app.get('/health')
        assert response.status_code == 200

    @mock.patch('requests.post')
    def test_complete(self, mock_post):
        case_number = 'GOODCASE001'
        mock_post.side_effect = self.mock_complete_application
        headers = {'content-Type': 'application/json'}
        response = self.app.get('/complete/%s' % case_number, headers=headers)
        assert response.status_code == 200

    @mock.patch('application.routes.get_title_from_working_register')
    @mock.patch('application.routes.update_title_on_working_register')
    def test_amend_entry(self, mock_update, mock_get):
        mock_update.side_effect = self.mock_update_title_on_working_register
        mock_get.side_effect = self.mock_get_title_from_working_register
        headers = {'content-Type': 'application/json'}
        response = self.app.post('/titles/dn100/groups/1/entries/1', data=ENTRY_AMENDMENT, headers=headers)
        assert response.status_code == 200
        self.assertEqual('amendment made at group position 1, entry position 1', response.data.decode("utf-8"))
        self.assertEqual(self.mock_title, TITLE_WITH_AMENDED_ENTRY)


    @mock.patch('application.routes.get_title_from_working_register')
    @mock.patch('application.routes.update_title_on_working_register')
    def test_insert_entry(self, mock_update, mock_get):
        mock_update.side_effect = self.mock_update_title_on_working_register
        mock_get.side_effect = self.mock_get_title_from_working_register
        headers = {'content-Type': 'application/json'}
        response = self.app.put('/titles/dn100/groups/1/entries', data=ENTRY_INSERT, headers=headers)
        assert response.status_code == 201
        self.assertEqual('Insert made at group position 1, entry position 2', response.data.decode("utf-8"))
        self.assertEqual(self.mock_title, TITLE_WITH_INSERTED_ENTRY)

    @mock.patch('application.routes.get_title_from_working_register')
    @mock.patch('application.routes.update_title_on_working_register')
    def test_delete_entry(self, mock_update, mock_get):
        mock_update.side_effect = self.mock_update_title_on_working_register
        mock_get.side_effect = self.mock_get_title_from_working_register
        response = self.app.delete('/titles/dn100/groups/1/entries/0')
        assert response.status_code == 200
        self.assertEqual('Delete at group position 1, entry position 0', response.data.decode("utf-8"))
        self.assertEqual(self.mock_title, TITLE_WITH_DELETED_ENTRY)

    @mock.patch('application.routes.write_to_working_titles_database')
    @mock.patch('application.routes.check_title_exists')
    def test_add_title(self, mock_check, mock_write):
        mock_check.return_value = False
        mock_write.return_value = None
        headers = {"Content-Type": "application/json"}
        response = self.app.post('/titles', data=json.dumps({"title_number":"DN100"}), headers=headers)
        assert response.status_code == 200

    @mock.patch('application.routes.write_to_working_titles_database')
    @mock.patch('application.routes.check_title_exists')
    def test_add_title_already_exists(self, mock_check, mock_write):
        mock_check.return_value = True
        mock_write.return_value = None
        headers = {"Content-Type": "application/json"}
        response = self.app.post('/titles', data=json.dumps({"title_number":"DN100"}), headers=headers)
        assert response.status_code == 200

    @mock.patch('application.routes.get_title_from_working_register')
    def test_get_title(self, mock_get):
        mock_get.side_effect = self.mock_get_title_from_working_register
        response = self.app.get('/titles/dn100')
        response_json = json.loads(response.data.decode())
        self.assertEqual(get_target_json(), response_json)

    @mock.patch('application.routes.get_title_from_working_register')
    @mock.patch('application.routes.update_title_on_working_register')
    def test_insert_group(self, mock_update, mock_get):
        mock_update.side_effect = self.mock_update_title_on_working_register
        mock_get.side_effect = self.mock_get_title_from_working_register
        headers = {'content-Type': 'application/json'}
        response = self.app.put('/titles/dn100/groups', data=GROUP_INSERT, headers=headers)
        self.assertEqual('Insert made at group position 2', response.data.decode("utf-8"))
        assert response.status_code == 201
        self.assertEqual(self.mock_title, TITLE_WITH_INSERTED_EMPTY_GROUP)

    @mock.patch('application.routes.get_title_from_working_register')
    @mock.patch('application.routes.update_title_on_working_register')
    def test_delete_group(self, mock_update, mock_get):
        mock_update.side_effect = self.mock_update_title_on_working_register
        mock_get.side_effect = self.mock_get_title_from_working_register
        response = self.app.delete('/titles/dn100/groups/0')
        assert response.status_code == 200
        self.assertEqual('Delete at group position 0', response.data.decode("utf-8"))
        self.assertEqual(self.mock_title, TITLE_WITH_DELETED_GROUP)

    @mock.patch('application.routes.get_title_from_working_register')
    @mock.patch('application.routes.update_title_on_working_register')
    def test_amend_group_of_entries(self, mock_update, mock_get):
        mock_update.side_effect = self.mock_update_title_on_working_register
        mock_get.side_effect = self.mock_get_title_from_working_register
        headers = {'content-Type': 'application/json'}
        response = self.app.post('/titles/dn100/groups/0', data=GROUP_REPLACE, headers=headers)
        assert response.status_code == 200
        self.assertEqual('Group amended at group position 0', response.data.decode("utf-8"))
        self.assertEqual(self.mock_title, TITLE_WITH_REPLACED_GROUP)

    # @mock.patch('application.db.engine.connect')
    # def test_get_working_register(self, mock_connection):
    #     db_execute_mock = mock.Mock()
    #     mock_connection.return_value = db_execute_mock
    #     #mock_commit.side_effect = self.mock_update_title_on_working_register(TEST_REGISTER)
    #     response = self.app.get('titles/AV239038')
    #     assert response.status_code == 200
    #
    # @responses.activate
    # def test_get_no_result_from_working_register(self):
    #
    #     url = app.config['CURRENT_REGISTER_API']+'/register/AV239040'
    #     responses.add(responses.GET, url,
    #                   body=json.dumps(TEST_REGISTER2),
    #                   status=200, content_type='application/json')
    #     response = self.app.get('titles/AV239040')
    #
    #     assert response.status_code == 200

    def test_register_model(self):
        workingTitle = WorkingTitles(TEST_REGISTER)
        return workingTitle

    def insert_mock_title_onto_db(self):
        self.app.post('/titles',data=json.dumps(TEST_REGISTER),
                                headers={'content-type': 'application/json'})

    def mock_update_title_on_working_register(self, title_json):
        self.mock_title = title_json
        return 'updated'

    def mock_get_title_from_working_register(self, title_number, register_format=None):
        return get_target_json()

    def mock_complete_application(self, *args):
        return Response("complete success", 200)

    def do_nothing(self, *args):
        pass
