# Importar implementações do python
import sys
import time
import os

# Importar classes de módulos do projeto
from Reg import Reg
from ULA import ULA
from control_storage import Control_Storage
from instruction import Instruction
from main_memory import Main_Memory

# Importar funções de módulos do projeto
from binary import convert_to_decimal

"""Função responsável por chamar todas as outras funções e dar inicio ao programa"""
def main():
	# Recebe o nome do arquivo que deve ser carregado na memória principal
	file_path = sys.argv[1]

	# Variáveis de Registradores
	registers = Reg()

	# Variáveis da ULA
	ula = ULA()

	# Variáveis de armazenamento de controle
	cs = Control_Storage()
	instruction = None

	# Variáveis da Memória principal
	memory = Main_Memory(512)
	instruction = None


	# Carrega arquivo na memória principal
	if (memory.load_memory(file_path)):
<<<<<<< HEAD
		"""
		os.system('cls' if os.name == 'nt' else 'clear')
		print("\t\t\t\tArquivo carregando na memória.")
		time.sleep(1)
		os.system('cls' if os.name == 'nt' else 'clear')
		print("\t\t\t\tArquivo carregando na memória..")
		time.sleep(1)
		os.system('cls' if os.name == 'nt' else 'clear')
		print("\t\t\t\tArquivo carregando na memória...")
		time.sleep(1)
		os.system('cls' if os.name == 'nt' else 'clear')
		"""
=======
		print("Deu certo")
		os.system('cls' if os.name == 'nt' else 'clear')
		# print("\t\t\t\tArquivo carregando na memória.")
		# time.sleep(1)
		# os.system('cls' if os.name == 'nt' else 'clear')
		# print("\t\t\t\tArquivo carregando na memória..")
		# time.sleep(1)
		# os.system('cls' if os.name == 'nt' else 'clear')
		# print("\t\t\t\tArquivo carregando na memória...")
		# time.sleep(1)
		# os.system('cls' if os.name == 'nt' else 'clear')

	print(f"Memória: {memory.get_memory_arr()}")
>>>>>>> c1e2ca59de3f37d0797b8400288e786346cada13

	while True:
		wait_for_clock()

		####################################### PARTE 1: Decodificar #####################################
		

		# Define a primeira instrução do microprograma a ser executada
		instruction = cs.get_readable_instruction()
		instruction_str_test = cs.get_readable_instruction("string")  # teste
		instruction_hex = cs.get_instruction().get_byte_instruction()
		print(f"Instrução: {instruction_str_test}")  # teste
		print(f"Instrução hex: {instruction_hex}")
		print(f"Partes: {instruction}") # teste

		####################################### PARTE 2: Barramentos #####################################
		b = registers.get_register_for_bus_b(instruction["bus_b"])
<<<<<<< HEAD
=======
		print(f"Registradores: {registers.dict}")
>>>>>>> c1e2ca59de3f37d0797b8400288e786346cada13

		####################################### PARTE 3: ULA #############################################

		ula.set_inputs(registers.get_register_by_name("h"), b)

		InstULA = instruction["ula"]

		ula.set_instruction(InstULA)

		ula.execute_instruction()

		####################################### PARTE 4: Registradores ####################################

		C = instruction["bus_c"]
		registers.set_register_by_inst(C, ula.get_result())
		
		####################################### PARTE 5: Memoria ##########################################
		m = instruction["memory"]

		if (m[0] == "1"):
			m_address = registers.get_register_by_name("mar")
			m_data = registers.get_register_by_name("mdr")
			m_data = int.from_bytes(m_data, "little")
			memory.write_memory(m_data, m_address*4)
	
		if (m[1] == "1"):
			m_address = registers.get_register_by_name("mar")
			m_data = memory.read_memory(m_address*4, 4)["byte"]
			m_data = int.from_bytes(m_data, "little")
			registers.set_register_by_name("mdr", m_data)

		if (m[2] == "1"):
			m_address = registers.get_register_by_name("pc")
			m_data = memory.fetch(m_address)["byte"]
			m_data = int.from_bytes(m_data, "little")
			registers.set_register_by_name("mbr", m_data)

		# print(memory.read_memory(256, 4))
		# print(memory.write_memory(265, 256))
		# print(memory.read_memory(256, 4))
		# print(memory.fetch(256))
		# print(memory.fetch(257))
		# print(memory.read_memory(4, 4))
		# print(memory.read_memory(8, 4))
		# print(memory.read_memory(12, 4))
		# print(memory.read_memory(16, 4))

			

		####################################### PARTE 6: Jumps ############################################
		NextAdress = convert_to_decimal(instruction["next_address"])

		J = instruction["jam"]

		if(J[0] == '1'):
			NextAdress = NextAdress | registers.get_register_by_name("mbr")
		if(J[1] == '1' and (not ula.is_zero()) and NextAdress < 256):
			NextAdress += 256
		if(J[2] == '1' and ula.is_zero() and NextAdress < 256):
			NextAdress += 256

		####################################### PARTE 7: NEXT ADDRESS #####################################
		print(f"Registradores: {registers.dict}")
		# Vai para a próxima instrução
		cs.next(NextAdress)


def wait_for_clock():
	""" Entrada: Nada
			Operacao: Pausa o programa ate que a tecla enter seja pressionada,
								utilizada para separar os ciclos do clock durante a execucao das instrucoes
			Saida: Nada """

	input("")

main()
