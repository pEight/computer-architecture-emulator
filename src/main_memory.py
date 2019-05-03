from reader import get_file_content
from binary import convert_to_bin, convert_to_decimal

"""Uma classe representando a memória principal"""
class Main_Memory:
	def __init__(self, size):
		"""Inicializa um objeto Main_Memory. Cria uma memória principal
		e ocupa todas as posições da memória com 0
		
		Keyword arguments:
		size -- Tamanho da memória principal
		"""
		self._memory = [b"\x00"]*size

	def get_memory_size(self): return len(self._memory)

	# Criado para teste. Remover depois	
	def get_memory(self): return self._memory

	# Criado para teste. Remover depois		
	def get_memory_int(self):
		def convert_to_int(elem):
			return int.from_bytes(elem, byteorder="little")

		dictionary = map(convert_to_int, self._memory)
		return list(dictionary)
	
	# Criado para teste. Remover depois	
	def get_memory_str(self):
		def convert_to_str(elem):
			return convert_to_bin(elem)["bin_str"]

		dictionary = map(convert_to_str, self.get_memory_int())
		return list(dictionary)

	# Criado para teste. Remover depois	
	def get_memory_arr(self):
		def convert_to_arr(elem):
			return convert_to_bin(elem)["bin_arr"]

		dictionary = map(convert_to_arr, self.get_memory_int())
		return list(dictionary)

	def load_memory(self, file_path):
		"""Ler uma informação e escrever na memória partindo da posição 1.
		Retorna True se a operação foi bem sucedida, False caso contrario.
		
		Keyword arguments:
		file_path -- Caminho do arquivo a ser escrito na memória
		"""
		file_content = get_file_content(file_path)

		if (file_content["size"] > self.get_memory_size()):
			return False

		return self.write_memory(file_content["bytes"], 1)

	def read_memory(self, position, lines=1):
		"""Ler uma posição ou mais posição de memória.
		Retorna um dicionário com a informação lida em bytes, string e array.

		Keyword arguments:
		position -- Posição inicial de memória a ser lida
		lines -- Número de posições a ser lida a partir de position
		"""
		if (position >= self.get_memory_size()):
			return None

		pos = None
		if (type(position) == str):
			pos = convert_to_decimal(position)
		elif (type(position) == bytes):
			pos = int.from_bytes(position, byteorder="little")
		else:
			pos = position

		result_byte = b""
		for i in range(0, lines):
			result_byte += self._memory[pos+i]

		result_str = ''
		for i in range(0, lines):
			int_value = int.from_bytes(self._memory[pos+i], "little")
			result_str += convert_to_bin(int_value)["bin_str"]

		result_arr = []
		for i in range(0, lines):
			int_value = int.from_bytes(self._memory[pos+i], "little")
			result_arr += convert_to_bin(int_value)["bin_arr"]

		return {
			"byte": result_byte,
			"str": result_str,
			"arr": result_arr
		}

	def write_memory(self, value, position):
		"""Escreve na memória um valor na posição position.
		Retorna True se a operação foi bem sucedida, False caso contrário.
		
		Keyword arguments:
		value -- Valor a ser escrito na memória
		position -- Posição de memória que value será escrito
		"""
		pos = None
		if(type(position) == str):
			pos = convert_to_decimal(position)
		elif(type(position) == bytes):
			pos = int.from_bytes(position, "little")
		else:
			pos = position

		result = None
		if (type(value) == str):
			result = convert_to_decimal(value)
		elif (type(value) == bytes):
			result = value
		else:
			result = value.to_bytes(value.bit_length(), "little")

		print(result)
		
		result_size = len(result)

		if (pos+result_size >= self.get_memory_size()):
			return False

		for i in range(0, result_size):
			self._memory[pos+i] = result[i].to_bytes(1, "little")

		return True

	def fetch(self, position):
		"""Busca um valor na posição position.
		Retorna o valor procurado.
		
		Keyword arguments:
		position -- Posição a ser procurada
		"""
		return self.read_memory(position)

# mem = Main_Memory(512)

# print(mem.load_memory("bin/prog.exe"))

# wasWritten = mem.write_memory(b"\x0A\x0B", 4)
# print(f"Esceveu na memória? {wasWritten}")
# print(f"Valor lido: {mem.read_memory(4, 2)}")

# print(f"Tamanho: {len(mem.get_memory())}")
# print(f"Memoria: {mem.get_memory()}")

# print(f"Tamanho str: {len(mem.get_memory_str())}")
# print(f"Memoria str: {mem.get_memory_str()}")

# print(f"Tamanho arr: {len(mem.get_memory_str())}")
# print(f"Memoria arr: {mem.get_memory_str()}")
