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
    b = registers.get_register_b(instruction['bus_b'])

    ####################################### PARTE 3: ULA #############################################

    ula.set_inputs(registers.get_register("h"), b)

    # Recebe instrucao da ula TEMPORARIO SERA FEITO NA PARTE 1
    instrucao = "10111100"
    ula.set_instruction(instrucao)

    ula.execute_instruction()

    if(ula.is_zero()):
      Zero = True
    if(not ula.is_zero()):
      Zero = False
    NonZero = not Zero

    ####################################### PARTE 4: Registradores ####################################

    # Recebe registrador para ser gravado, sendo ele representado pelos bits C
    C = "000000100"
    for i in range(0, len(C)):
      registers.set_register(i, ula.get_result())

    ####################################### PARTE 5: Memoria ##########################################

    ####################################### PARTE 6: Jumps ############################################

    ####################################### PARTE 7: NEXT ADDRESS #####################################
      # Vai para a próxima instrução
    cs.next()


def wait_for_clock():
  """ Entrada: Nada
      Operacao: Pausa o programa ate que a tecla enter seja pressionada,
                utilizada para separar os ciclos do clock durante a execucao das instrucoes
      Saida: Nada """

  input("")

main()
