from reader import get_file_content
from binary import convert_to_bin, convert_to_decimal

class Memory:
	def __init__(self, memory_size, word_size):
		self._memory_size = memory_size
		self._word_size = word_size

		while(self._memory_size % self._word_size != 0):
			self._memory_size+=1
		
		self._memory = bytearray(b"\x00"*self._word_size)*self._memory_size
		self._memory_str = self._define_memory_str()
		self._memory_arr = self._define_memory_arr()

	def get_memory(self): return self._memory
	def get_memory_str(self): return self._memory_str
	def get_memory_arr(self): return self._memory_arr
	def get_memory_size(self): return self._memory_size
	def get_word_size(self): return self._word_size

	def write_value(self, value, position):
		def write(write_value):
			b = bytes([write_value])
			pos = None

			if(type(position) == 'str'):
				pos = convert_to_decimal(position)
			else:
				pos = position
			
			if (pos+len(b) > self._memory_size): return False
			for i in range(0, len(b)):
				self._memory[pos+i] = b[i]
			return True

		if (type(value) == 'int'):
			return write(value)

		int_value = convert_to_decimal(value)
		return write(int_value)

	def read_value(self, position, n_bytes=1):
		pos = None
		if (type(position) == 'str'):
			pos = convert_to_decimal(position)
		else:
			pos = position

		result = ''
		for i in range(0, n_bytes):
			result += convert_to_bin(self._memory[pos+i])
		
		return result

	def fetch_value(self, value):
		return 0		
	
	def _define_memory_str(self):
		def define_str(elem):
			return convert_to_bin(elem)["bin_str"]

		dictionary = map(define_str, self._memory)
		return list(dictionary)

	def _define_memory_arr(self):
		def define_arr(elem):
			print(type(elem))
			return convert_to_bin(elem)["bin_arr"]

		dictionary = map(define_arr, self._memory)
		return list(dictionary)

	def load_file(self, file_path):
		file_content = get_file_content(file_path)
		size = file_content["size"]

		for i in range(0, size):
			self._memory[i] = file_content["byte"][i]
			return True

		return False

mem = Memory(512, 4)
print(mem.get_memory_str())

print(mem.write_value(1, 3))

