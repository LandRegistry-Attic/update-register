import unittest
import json
import mock

from application import app
from test_data import TARGET, TITLE_WITH_AMENDED_ENTRY, ENTRY_AMENDMENT


class TestCaseListView(unittest.TestCase):

    mock_title = {}

    def setUp(self):
        self.app = app.test_client()

    def test_service_health(self):
        response = self.app.get('/health')
        assert response.status_code == 200


    @mock.patch('application.routes.get_title_from_working_register')
    @mock.patch('application.routes.update_title_on_working_register')
    def test_amend_entry(self, mock_update, mock_get):
        mock_update.side_effect = self.mock_update_title_on_working_register
        mock_get.side_effect = self.mock_get_title_from_working_register
        headers = {'content-Type': 'application/json'}
        response = self.app.post('/titles/dn100/groups/1/entries/1', data=ENTRY_AMENDMENT, headers=headers)
        assert response.status_code == 200
        self.assertEqual(self.mock_title, TITLE_WITH_AMENDED_ENTRY)

    def test_insert_entry(self):
        headers = {'content-Type': 'application/json'}
        response = self.app.put('/titles/dn100/groups/1/entries/1', data='{"a":"1"}',
                                headers=headers)
        assert response.status_code == 201
        self.assertEqual('wip insert', response.data.decode("utf-8"))

    def test_delete_entry(self):
        headers = {'content-Type': 'application/json'}
        response = self.app.delete('/titles/dn100/groups/1/entries/1', data='{"a":"1"}',
                                   headers=headers)
        assert response.status_code == 200
        self.assertEqual('wip delete', response.data.decode("utf-8"))

    def test_amend_group_entry(self):
        headers = {'content-Type': 'application/json'}
        response = self.app.post('/titles/dn100/groups/1/entries/', data='{"a":"1"}',
                                 headers=headers)
        assert response.status_code == 200
        self.assertEqual('wip group amend', response.data.decode("utf-8"))

    def mock_update_title_on_working_register(self, title_json):
        self.mock_title = title_json
        return 'updated'

    def mock_get_title_from_working_register(self, title_number):
        return TARGET

