from unittest import TestCase
from unittest.mock import MagicMock
from hw1 import read_data, dates, paginate
import json

class TestHw1(TestCase):
	@classmethod
	def setUpClass(cls):
		cls.sample_data = [
			{ 'id': 0, 'year': 1980, 'rain': 32.0 },
			{ 'id': 1, 'year': 1981, 'rain': 35.5 },
			{ 'id': 2, 'year': 1982, 'rain': 33.3 },
			{ 'id': 3, 'year': 1983, 'rain': 36.7 }
		]

	def test_read_data(self):
		result = read_data()
		self.assertEqual(json.dumps(result), json.dumps(self.sample_data))

	def test_dates(self):
		result = dates(self.sample_data)
		self.assertEqual(len(result), len(self.sample_data))

	def test_dates_start(self):
		result = dates(self.sample_data, start=1982)
		for data in result:
			self.assertGreaterEqual(data['year'], 1982)

	def test_dates_end(self):
		result = dates(self.sample_data, end=1981)
		for data in result:
			self.assertLessEqual(data['year'], 1981)

	def test_dates_start_end(self):
		result = dates(self.sample_data, start=1981, end=1983)
		for data in result:
			self.assertGreaterEqual(data['year'], 1981)
			self.assertLessEqual(data['year'], 1983)
	
	def test_paginate(self):
		result = paginate(self.sample_data)
		self.assertEqual(len(result), len(self.sample_data))
	
	def test_paginate_offset(self):
		result = paginate(self.sample_data, offset=1)
		for data in result:
			self.assertGreaterEqual(data['id'], 1)		

	def test_paginate_limit(self):
		result = paginate(self.sample_data, limit=3)
		self.assertLessEqual(len(result), 3)
	
	def test_paginate_offset_limit(self):
		result = paginate(self.sample_data, offset=1, limit=2)
		for data in result:
			self.assertGreaterEqual(data['id'], 1)
		self.assertLessEqual(len(result), 2)	








