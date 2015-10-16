#
#	extract.py
#	parser to reorg file data based on the format file
#
#

import os
import csv


class File(object):

	@classmethod
	def get_delimiter(cls):
		return getattr(cls, 'delimiter', ',')

	@classmethod
	def is_valid(cls, _file):
		if not os.path.isfile(_file):
			raise Exception('File {} not found error'.format(_file))
		return _file

	def __init__(self, file_loc):
		self.file_loc = file_loc

	def read(self):
		with open(self.file_loc, 'r') as f:
			for row in csv.reader(f, delimiter=self.get_delimiter()):
				yield row


class FormatFile(File):
	delimiter = ','


class DataFile(File):
	delimiter = '\n'


class Format(object):
	TYPES = {
		'string': lambda str: str.replace(' ', ''),
		'boolean': lambda v: bool(int(v)),
		'integer': int,
	}

	def __init__(self, name, width, type, *args):
		self.name = name
		self.width = int(width)
		self.type = type

	def get_value(self, value):
		if self.type in self.TYPES:
			return self.TYPES.get(self.type)(value)
		return value


class Extractor(object):

	@classmethod
	def parse_from_file(cls, format_file, data_file):
		iformat = FormatFile(format_file).read()
		idata = DataFile(data_file).read()
		return cls(iformat, idata).get_parsed_data()

	def __init__(self, iformat, idata):
		self.format_data = iformat
		self.data = idata

	def parse_format(self):
		# ignore the header
		names = next(self.format_data, None)
		if names is None:
			raise Exception("invalid csv file")

		for row in self.format_data:
			yield Format(*row)

	def parse_data(self, formatters):
		for row in self.data:
			row = row[0]
			index = 0
			_d = {}
			for format in formatters:
				_d[format.name] = format.get_value(row[index: index + format.width])
				index = index + format.width
			yield _d

	def get_parsed_data(self):
		formatters = list(self.parse_format())
		return list(self.parse_data(formatters))


def parse_flat_file(data_filename=None, format_filename=None):
	data_filename = data_filename or 'fixtures/data.txt'
	format_filename = format_filename or 'fixtures/format.csv'
	return Extractor.parse_from_file(data_filename, format_filenmae)
