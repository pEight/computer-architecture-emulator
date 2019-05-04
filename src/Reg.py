from binary import convert_to_decimal

class Reg:

	def __init__(self):
		"""Inicializa um objeto Reg que armazenará todos os registradores"""
		self.dict = {
			"h": 0,
			"opc": 0,
			"tos": 0,
			"cpp": 0,
			"lv": 0,
			"sp": 0,
			"pc": 0,
			"mdr": 0,
			"mar": 0,
			"mbr": 0
		}

	def get_register_by_name(self, register_name):
		"""Retorna o valor do registrador especificado pelo nome
		
		Keyword arguments:
		register_name -- o nome do registrador desejado(string)
		"""

		#Caso de escape, talvez nao seja necessario
		#if(register_name == "none"): return 0

		return self.dict[register_name]

	def set_register_by_name(self, register_name, value):
		"""Altera o valor do registrador especificado pelo nome
		
		Keyword arguments:
		register_name -- o nome do registrador desejado (string)
		value -- o valor a ser atribuido ao registrador (int)
		"""

		self.dict[register_name] = value


	def set_register_by_inst(self, instruction_string, value):
		"""Grava o valor recebido nos registradores, especificados atraves da 
		parte C da instrucao recebida
		
		Keyword arguments:
		instruction_string -- a string que representa a parte C da instrucao (string)
		value -- o valor a ser atribuido aos registradores (int)
		"""

		for i in range(0, len(instruction_string)):
		 if(instruction_string[i] == '1'):
				self.dict[self.dict.keys()[index]] = value
		

	def get_register_for_bus_b(self, instruction_string):
		"""Retorna o valor que o barramento B recebera atraves da parte B 
		da instrucao em forma de string
		
		Keyword arguments:
		instruction_string -- a string que representa a parte B da instrucao (string)
		"""

		#Talvez seja necessario inverter a string
		#inv_reg = instruction_string[::-1]

		intRegister = convert_to_decimal(inv_reg)

		reg_names_for_b = ["mdr", "pc", "mbr", "mbr", "sp", "lv", "cpp", "tos", "opc"]

		reg_value = self.dict[reg_names_for_b[intRegister]]

		#Retorna o valor de MBR com sinal
		if(intRegister == 2 and reg_value & (0b10000000)):
			reg_value = reg_value | (0b111111111111111111111111 << 8)

		return reg_value
