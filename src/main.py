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
	Zero = True
	NonZero = False

	# Variáveis de armazenamento de controle
	cs = Control_Storage()
	instruction = None

	# Variáveis da Memória principal
	memory = Main_Memory(512)
	instruction = None

	# Carrega arquivo na memória principal
	if (memory.load_memory(file_path)):
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

	while True:
		wait_for_clock()

		####################################### PARTE 1: Decodificar #####################################
		

		# Define a primeira instrução do microprograma a ser executada
		instruction = cs.get_readable_instruction()
		instruction_str_test = cs.get_readable_instruction("string")  # teste
		print(f"Instrução: {instruction_str_test}")  # teste
		print(f"Partes: {instruction}") # teste

		####################################### PARTE 2: Barramentos #####################################
		b = registers.get_register_for_bus_b(instruction.get_bus_b_bin())

		####################################### PARTE 3: ULA #############################################

		ula.set_inputs(registers.get_register_by_name("h"), b)

		InstULA = instruction.get_ula_bin()

		ula.set_instruction(InstULA)

		ula.execute_instruction()

		####################################### PARTE 4: Registradores ####################################

		C = instruction.get_bus_c_bin()
		registers.set_register_by_inst(C, ula.get_result())
		
		####################################### PARTE 5: Memoria ##########################################
		

		####################################### PARTE 6: Jumps ############################################
		NextAdress = instruction.get_next_address_bin()

		J = instruction.get_jam_bin()

		if(J[0] == '1'):
			NextAdress = NextAdress | registers.get_register_by_name("mbr")
		if(J[1] == '1' and (not ula.is_zero())):
			NextAdress += 256
		if(J[2] == '1' and ula.is_zero()):
			NextAdress += 256

		####################################### PARTE 7: NEXT ADDRESS #####################################
			# Vai para a próxima instrução
		cs.next(NextAdress)


def wait_for_clock():
	""" Entrada: Nada
			Operacao: Pausa o programa ate que a tecla enter seja pressionada,
								utilizada para separar os ciclos do clock durante a execucao das instrucoes
			Saida: Nada """

	input("")

main()
