import unittest
import requests
import json
import random

class TestServer(unittest.TestCase):

    # Check that the server gives a list of all candidates.
    def test_gives_list(self):
        d = requests.get('http://qainterview.cogniance.com/candidates')
        code = d.status_code
        obj = json.loads(d.text)
        self.assertEqual(code, 200)

        size = len(obj['candidates'])
        self.assertTrue(size > 0)

    # Check that the server add new candidate.
    def test_add_new_candidate(self):
        load = {'name': 'Masha', 'position': 'QA intern'}
        json_params = json.dumps(load)
        headers = {'content-type': 'application/json'}
        r = requests.post('http://qainterview.cogniance.com/candidates', data=json_params, headers=headers)
        code = r.status_code
        self.assertEqual(code, 201)


    # Check negative verifications.
    def test_incorrect_add_data(self):
        load = {'dogName': 'Bill', 'catName': 'Sarah', 'parrotName': 'Kluv'}
        json_params = json.dumps(load)
        headers = {'content-type': 'application/json'}
        b = requests.post('http://qainterview.cogniance.com/candidates', data=json_params, headers=headers)
        code = b.status_code
        self.assertEqual(code, 400)

    # get the candidate.
    def test_get_one_candidate(self):
        load = {'name': 'Masha3', 'position': 'test position'}
        json_params = json.dumps(load)
        headers = {'content-type': 'application/json'}
        rs = requests.post('http://qainterview.cogniance.com/candidates', data=json_params, headers=headers)
        obj = json.loads(rs.text)
        new_candidate = obj['candidate']
        new_candidate_id = new_candidate['id']

        url = ('http://qainterview.cogniance.com/candidates/'+str(new_candidate_id))
        k = requests.get(url)
        self.assertEqual(k.status_code, 200)
        obj = json.loads(k.text)

        self.assertEqual(obj['candidate']['id'], new_candidate_id, 'Returns incorrect id')
        self.assertEqual(obj['candidate']['name'], 'Masha3', 'Returns incorrect name')
        self.assertEqual(obj['candidate']['position'], 'test position', 'Returns incorrect position')

    # get wrong candidate with id
    def test_get_one_wrong_candidate(self):
        url = ('http://qainterview.cogniance.com/candidates/'+str(random.randint(9999, 99999)))
        k = requests.get(url)
        self.assertEqual(k.status_code, 404)

    # get wrong candidate with id as string
    def test_get_one_wrong_string_candidate(self):
        url = ('http://qainterview.cogniance.com/candidates/'+'WrongPath')
        k = requests.get(url)
        self.assertEqual(k.status_code, 404)

    # Delete the candidat.
    def test_delete_candidate(self):
        load = {'name': 'Masha', 'position': 'QA intern'}
        json_params = json.dumps(load)
        headers = {'content-type': 'application/json'}
        rs = requests.post('http://qainterview.cogniance.com/candidates', data=json_params, headers=headers)
        obj = json.loads(rs.text)
        new_candidate = obj['candidate']
        new_candidate_id = new_candidate['id']
        url = ('http://qainterview.cogniance.com/candidates/'+str(new_candidate_id))
        k = requests.delete(url)
        code = k.status_code
        self.assertEqual(code, 200)


unittest.main()