import extract.py

def parser(df, ff):

	ff_d = []
	with open('ff') as f:
		i = 0
		head = []
		for line in f:
			if i == 0:
				head = line.split(',')
			else:
				ff_d.append(zip(head, line.split(',')))

	with open('ff') as f:
		for line in f:
			_d = {}
			index = 0
			for v in ff_d:
				name, width, dt = v
				if dt[1] == 'string':
					value = line[index:index + width[1]]

				if dt[1] == 'int':
					value = int(line[index:index + width[1]])

				if dt[1] == 'bool':
					value = bool(int(line[index:index + width[1]])

				_d[name[1]] = value
				index = width
			yield _d


if __name__ == '__main__':
	'''
		python extract.py -d path/to/dat/file.txt -f /path/to/format/file.csv
	'''

	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument("-d", dest="data", help="data file", type=File.is_valid,
			required=True, metavar="FILE")
	parser.add_argument("-f", dest="format", help="format file", type=File.is_valid,
			required=True, metavar="FILE")

	args = parser.parse_args()
	print Extractor.parse_from_file(args.format, args.data)
