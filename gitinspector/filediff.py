import os

from gitinspector import extensions


class FileDiff(object):
	def __init__(self, string):
		commit_line = string.split("|")

		if commit_line.__len__() == 2:
			self.name = commit_line[0].strip()
			self.insertions = commit_line[1].count("+")
			self.deletions = commit_line[1].count("-")

	@staticmethod
	def is_filediff_line(string):
		string = string.split("|")
		return string.__len__() == 2 and string[1].find("Bin") == -1 and ('+' in string[1] or '-' in string[1])

	@staticmethod
	def get_extension(string):
		string = string.split("|")[0].strip().strip("{}").strip("\"").strip("'")
		return os.path.splitext(string)[1][1:]

	@staticmethod
	def get_filename(string):
		return string.split("|")[0].strip().strip("{}").strip("\"").strip("'")

	@staticmethod
	def is_valid_extension(string):
		extension = FileDiff.get_extension(string)

		for i in extensions.get():
			if (extension == "" and i == "*") or extension == i or i == '**':
				return True
		return False
