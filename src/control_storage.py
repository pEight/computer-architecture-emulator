from instruction import Instruction
from reader import get_file_content
from binary import convert_to_decimal, convert_to_bin

"""Uma classe que representa o Armazenamento de Controle de 512 bytes"""
class Control_Storage:
	def __init__(self):
		"""Inicializa um objeto Armazenamento de Controle"""
		# Ler microprog.rom
		file_content = get_file_content("bin/microprog.rom")

		self._cs_bytes = [
			file_content["bytes"][i:i+8] for i in range(0, file_content["size"], 8)
		]
		self._cs_pos = 0
		self._instruction = Instruction(self._cs_bytes[self._cs_pos])

	def get_readable_instruction(self, instruction_type="dictionary"):
		"""Retorna uma instrução de uma legível para um estudante de arquitetura
		de computadores.
		
		Keyword arguments:
		instruction_type -- o tipo que a instrução deve estar(string, list, dictionary)
		"""
		if (instruction_type == "string"):
			return self._instruction.get_str_instruction()
		if(instruction_type == "list"):
			return self._instruction.get_arr_instruction()
		return self._instruction.get_dict_instruction()
		

	def get_instruction(self):
		"""Retorna um objeto instrução que a posição do armazenamento
		de controle se encontra"""
		return self._instruction

	def _set_instruction(self, position):
		"""Define a instrução para uma outra da memória do armazenamento de controle"""
		self._instruction = Instruction(self._cs_bytes[position])

	def next(self, next_address=""):
		"""Vai para a próxima instrução e retorna True caso a operação seja
		bem sucedida e False caso contrário"""
		instruction = self.get_readable_instruction()

		if (next_address == ""):
			self._cs_pos = convert_to_decimal(instruction["next_address"])
			self._set_instruction(self._cs_pos)
			return True
		
		if (type(next_address) == int):
			self._cs_pos = next_address
			self._set_instruction(self._cs_pos)
			return True

		if (type(next_address) == str):
			self._cs_pos = convert_to_decimal(next_address)
			self._set_instruction(self._cs_pos)
			return True

		return False

cs = Control_Storage()

pos119 = cs._cs_bytes[119]
for i in pos119:
	print(i)

# pos120 = cs._cs_bytes[120]
# pos121 = cs._cs_bytes[121]




# print(f"120: {pos119}")
# print(f"120: {pos120}")
# print(f"120: {pos121}")

