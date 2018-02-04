# =============================================================================

class FileReader(object):
	__path = None
	__file = None
	__content_lines = None
	__cur_line = -1
	__EOF = False
	__iter = None

	def __init__(self, path):
		self.__path = path
		self.read()

	def read(self):
		if self.__path is None:
			raise Exception("file path is missing")
		self.__file = open(self.__path, 'r')
		self.__content_lines = self.__file.readlines()
		self.__iter = iter(self.__content_lines)
		self.__cur_line = 

	def next_line(self):
		if self.__file is None:
			raise Exception("file not initialized !!")
		try:
			line = next(self.__iter)
			self.__cur_line += 1
			return line
		except StopIteration as e:
			self.__EOF = True
			return -1

	def get_current_line(self):
		return self.get_line(self.__cur_line)

	def get_line(self, line_num):
		if line_num < 0 or line_num > len(self.__content_lines):
			raise Exception("get_line: out of bound ERROR !!")
		if self.__file is None:
			raise Exception("get_line ERROR")
		return self.__content_lines[line_num - 1]

	def close(self):
		if self.__file is not None:
			self.__file.close()
			self.__file = None
			self.__cur_line = -1
			self.__iter = None

	def EOF(self):
		return self.__EOF == True

	def cur_line_index(self):
		return self.__cur_line

# END OF FR CLASS
# =============================================================================

fr = FileReader("D:\\tmp.txt")
line = fr.next_line()
while not fr.EOF():
	# TODO: write your code here

	line = fr.next_line()

fr.close()