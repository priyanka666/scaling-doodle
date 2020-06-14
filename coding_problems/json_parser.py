
# !/bin/python3
class Token:
	STRING_BEGIN = STRING_END = '"'
	LIST_BEGIN = '['
	LIST_END = ']'
	LIST_DELIMITER = DICT_DELIMITER = ','
	DICT_SYMBOL = ':'
	DICT_BEGIN = '{'
	DICT_END = '}'
	WHITESPACE = ' '
	NEWLINE = '\n'


class ParserException(Exception):
	pass


def isdigit(s):
	return s in "01234567890"


def parse_number(string):
	number = ""
	index = 0
	while index < len(string) and isdigit(string[index]):
		number += string[index]
		index += 1
	return int(number), string[index:]


def parse_string(string):
	# write your code here
	for index, char in enumerate(string):
		if char == Token.STRING_END and index != 0:
			return ((string[1:index], string[index + 1:]))


def parse_list(string):
	# write your code here
	# a = list()
	brackets = list()
	b = None
	for index, char in enumerate(string):

		if char == ',':
			continue

		if char == Token.LIST_BEGIN:
			if index == 0:
				a = list()
			else:
				if len(brackets) == 1:
					b = list()
				elif b is not None:
					b = [b]
			brackets.append('[')
			continue

		if char == Token.LIST_END:

			if len(brackets) > 1:
				brackets.pop()
				if len(brackets) == 1:
					a.append(b)
			else:
				return (a, string[index + 1:])

			continue

		if isdigit(string[index]) and index != 0:
			a.append(int(char))
		else:
			a.append(char)


def parse_dict(string):
	d = dict()
	key_start = 1
	already_done = []
	dictss = []
	for index, char in enumerate(string):
		if char == Token.DICT_BEGIN:
			dictss.append('{')
		if char == Token.DICT_END:
			dictss.pop()
			if len(dictss) == 0:
				return (d, string[index + 1:])

		if char == Token.DICT_SYMBOL:
			if string[index+1] == Token.LIST_BEGIN:
				gdsd = []
				for indd, char in enumerate(string[index:]):
					if char == Token.LIST_BEGIN:
						gdsd.append('[')
					if char == Token.LIST_END:
						gdsd.pop()
						if len(gdsd) == 0:
							value = parse_list(string[index + 1:index + indd+1])[0]
							d[string[key_start + 1:index - 1]] = value
							key_start = index + indd + 1
							break

			elif string[index+1] == Token.DICT_BEGIN:
				for indd, char in enumerate(string[index:]):
					if char == Token.DICT_END:
						value = parse_dict(string[index + 1:index + indd+1])[0]
						d[string[key_start+2:index - 1]] = value
						key_start = index + indd + 1
						already_done = already_done + (range(index + 1, index + indd+1))
						break
			else:
				if index in already_done:
					continue
				for indd, char in enumerate(string[index:]):
					if char == Token.DICT_DELIMITER or index + indd == len(string) - 1:
						value_parse = string[index + 1:index + indd]

						if isdigit(value_parse):
							value = int(value_parse)
						else:
							value = value_parse
						# print "value_parse", value_parse
						# value = int(string[index + 1:index + indd]) if isdigit(string[index + 1:index + indd]) \
						# 	else string[index + 1:index + indd]
						# print ('key', key_start + 1, index - 1)
						d[string[key_start + 1:index-1]] = value
						key_start = index + indd + 1
						break


def parse(string):

	if string[0] == Token.STRING_BEGIN:
		return parse_string(string)

	elif string[0] == Token.LIST_BEGIN:
		return parse_list(string)

	elif string[0] == Token.DICT_BEGIN:
		return parse_dict(string)

	else:
		return parse_number(string)


if __name__ == '__main__':
	input_list = [
		'123',
		'123abc',
		'"123"abc',
		'"abc"[123]',
		'[1,2,3]',
		'[1,2,3][abc]',
		'[[[]]]',
		'[[],[[]]]',
		'["a",123,["x","y"]]',
		'{"a":1}',
		'{"a":1,"b":2}',
		'{}',
		'{}abc',
		'{"a":[[[]]]}',
		'{"a":1,"b":[1,2,3],"c":{"d":1}}',
	]

	output_list = [
		(123, ''),
		(123, 'abc'),
		('123', 'abc'),
		('abc', '[123]'),
		([1, 2, 3], ''),
		([1, 2, 3], '[abc]'),
		([[[]]], ''),
		([[], [[]]], ''),
		(["a", 123, ["x", "y"]], ''),
		({"a": 1}, ''),
		({"a": 1, "b": 2}, ''),
		({}, ''),
		({}, 'abc'),
		({"a": [[[]]]}, ''),
		({"a": 1, "b": [1, 2, 3], "c": {"d": 1}}, ''),
	]

	total_test = len(input_list)
	test = 0
	while test < total_test:

		if parse(input_list[test]) == output_list[test]:
			print("passed")
		else:
			print("not_passed")
		test += 1
