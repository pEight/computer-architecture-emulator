class ULA:

	def __init__(self):
		"""Inicializa o objeto da ULA (Unidade Logica e Aritmetica)"""
		self.a = 0
		self.b = 0
		self.inst = 0
		self.result = 0
		self.zero = True

	def set_instruction(self, instruction_str):
		"""Altera a parte da instrucao que sera executada pela ULA
		
		Keyword arguments:
		instruction_str -- a string referente a parte de instrucao relativa a ula(string)
		"""

		self.shift = instruction_str[:2]
		self.inst = instruction_str[2:]

	def set_inputs(self, a, b):
		"""Altera o valor dos campos a e b da ULA
		Esses campos devem ser recebidos a partir de uma leitura de registradores
		
		Keyword arguments:
		a -- o valor que sera atribuido a entrada A da ULA(int)
		b -- o valor que sera atribuido a entrada B da ULA(int)
		"""

		self.a = a  # Receber o valor do registrador h
		self.b = b  # Recebe o valor de um registrador baseado no B

	def execute_instruction(self):
		"""Realiza na ULA os seguintes passos:
		1- Executa a instrucao armazenada na ULA
		2- Em seguida, registra no campo zero se a ula obteve resultado igual a Zero
		3- Realiza os deslocamentos de bits se necessário
		4- Altera o campo do resultado da ULA com o novo valor
		5- Retorna o valor do resultado da ULA
		"""

		# Todas as istrucoes da ULA
		instructions = ["011000", "010100", "011010", "101100", "111100", "111101", "111001", "110101", "111111", "110110", "111011", "001100", "011100", "010000", "110001", "110010"]

		# Os resultados relacionados a cada instrucao
		results = [self.a, self.b, ~ self.a, ~ self.b, self.a + self.b, self.a + self.b + 1, self.a + 1, self.b + 1, self.b - self.a, self.b - 1, -1*self.a, self.a & self.b, self.a | self.b, 0, 1, -1]

		if(instructions.index(self.inst) != -1):
			# Se a instrucao passada utilizar a ULA
			self.result = results[instructions.index(self.inst)]

		else:
			# Caso de escape caso a ULA nao deva fazer nada
			self.result = 0

		# Registra na ULA se o resultado antes do deslocamento era Zero
		self.zero = self.result == 0

		# Realiza os Deslocamentos
		if(self.shift == "01"):
			self.result = self.result >> 1

		if(self.shift == "10"):
			self.result = self.result << 8

		# Retorna o resultado
		return self.result
		
	def is_zero(self):
		"""Indica se o resultado obtido na ULA antes do deslocamento foi Zero ( 0 )
		"""
		return self.zero

	def get_result(self):
		"""Retorna o campo que armazena o resultado da ULA
		"""
		return self.result
