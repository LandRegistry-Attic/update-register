import unittest

from application import app


class TestCaseListView(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_service_health(self):
        response = self.app.get('/health')
        assert response.status_code == 200

    def test_amend_entry(self):
        headers = {'content-Type': 'application/json'}
        response = self.app.post('/titles/dn100/groups/1/entries/1', data='{"a":"1"}',
                                 headers=headers)
        assert response.status_code == 200
        self.assertEqual('wip amend', response.data.decode("utf-8"))

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