import unittest

from processing.extract_title import extract_title


class TestExtractLinks(unittest.TestCase):
	def test_extract_title(self):
		text = "# This is a title"
		title = extract_title(text)
		self.assertEqual("This is a title", title)
	
	def test_extract_title_no_title(self):
		text = "This is not a title"
		with self.assertRaises(ValueError):
			extract_title(text)