#
#	ut_extract.py
#
#

import unittest

from pyd.extract import (
	Format,
	FormatFile,
	DataFile,
	Extractor
)


class FormatTest(unittest.TestCase):

	def test_simple(self):
		'''
			get value for given type
		'''
		f = Format('name', '10', 'string')
		self.assertEqual('string+name', f.get_value('string+name'))

		f = Format('name', '1', 'boolean')
		self.assertEqual(True, f.get_value('1'))


class ExtractorTest(unittest.TestCase):

	def test_simple(self):
		'''
			get value for given type
		'''
		formatter = (
			f for f in (
				('Column name', '10', 'string'),
				('name', '10', 'string'),
				('valid', '1', 'boolean'),
				('count', '3', 'integer'),
			))

		data = (
			['Foonyor   1  1 dsafasdfafds'],
			['Barzane   0-12adsfa'],
			['Quuxitude 1103'],
		)

		parser = Extractor(formatter, data)
		self.assertEqual(parser.get_parsed_data(), [
			{'name': 'Foonyor', 'valid': True, 'count': 1},
			{'name': 'Barzane', 'valid': False, 'count': -12},
			{'name': 'Quuxitude', 'valid': True, 'count': 103},
		])

	def test_empty(self):
		'''
			get value for given type
		'''
		formatter = (
			f for f in (
				('Column name', '10', 'string'),
				('name', '10', 'string'),
				('valid', '1', 'boolean'),
				('count', '3', 'integer'),
			))

		parser = Extractor(formatter, [])
		self.assertEqual(parser.get_parsed_data(), [])


if __name__ == '__main__':
	unittest.main()
