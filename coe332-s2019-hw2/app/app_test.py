from unittest import TestCase
from app import app
import json

class TestFlask(TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_coe332(self):
        # Test the / root route
        result = self.client.get('/')

        # The http status code should be OK
        self.assertEqual(result.status, "200 OK")

        # Decode the binary result returned by the test client into a utf-8 string
        data_string = result.data.decode("utf-8")
        data_dictionary = json.dumps(data_string)

        # Assert that the returned structure has the data we want
        self.assertIn("instructors", data_dictionary)
        self.assertIn("meeting", data_dictionary)
        self.assertIn("assignments", data_dictionary)

    def test_instructors(self):
        # Test the /instructors route
        result = self.client.get('/instructors')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(len(result.json), 3)

    def test_instructor_ari(self):
        # Test the /instructors/1 route
        result = self.client.get('/instructors/1')
        self.assertEqual(result.status_code, 200)
        data = result.json
    #self.assertEqual(data['name'], "Ari Kahn")
        self.assertEqual(data['email'], "akahn@tacc.utexas.edu")

    def test_instructor_nobody(self):
        # Test the /instructors/4 route
        result = self.client.get('/instructors/4')
        self.assertEqual(result.status_code, 404)

    def test_assignments(self):
        # Test the /assignments route
        result = self.client.get('/assignments')
        self.assertEqual(result.status_code, 200)
        data = result.json
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['name'], "hw1")
        self.assertEqual(data[0]['url'], "https://bitbucket.org/jchuahtacc/coe332-f2019-hw1")

    def test_post_assignment(self):
        # Test that we can post a new assignment to /assignments
        # Testing json dictionary equivalence is weird, so we will make our best effort
        # Create a dictionary
        new_assignment = { 'name' : 'hw3', 'url' : 'https://bitbucket.org/jchuahtacc/coe332-f2019-hw3', 'points': 10 }

        # Post the string representation of the dictionary
        result = self.client.post('/assignments', json=new_assignment, content_type="application/json")
        self.assertEqual(result.status_code, 200)

        # Try getting all the assignments
        result = self.client.get('/assignments')
        self.assertEqual(result.status_code, 200)
        assignments = result.json

        # There should be more assignments now
        self.assertGreater(len(assignments), 2)

        # The last assignment retrieved should be our new assignment
        self.assertEqual(
            json.dumps(assignments[-1], sort_keys=True),
            json.dumps(new_assignment, sort_keys=True)
        )

    def test_meeting(self):
        # Test the /meeting route
        result = self.client.get('/meeting')
        self.assertEqual(result.status_code, 200)
        data = result.json
        self.assertEqual(data['start'], 1100)
        self.assertEqual(data['end'], 1330)
        self.assertEqual(data['location'], "GDC 3.248")
        

    def test_meeting_days(self):
        # Test the /meeting/days route
        result = self.client.get('/meeting/days')
        self.assertEqual(result.status_code, 200)
        data = result.json
        self.assertEqual(data[0], "Tuesday")
        self.assertEqual(data[1], "Thursday")

    def test_assignment_url(self):
        # Test the /assignments/0/url route
        result = self.client.get('/assignments/0/url')
        self.assertEqual(result.status_code, 200)
        data = result.json
        self.assertEqual(data, "https://bitbucket.org/jchuahtacc/coe332-f2019-hw1")
