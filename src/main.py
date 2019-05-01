# Arquivo principal
# Responsável por chamar todas as outras funcoes e dar inicio ao programa

import sys

from Reg import Reg
from ULA import ULA

from reader import get_file_content
from binary import convert_to_decimal
from control_storage import Control_Storage
from instruction import Instruction

def main():
  # Caminho passado na linha de comando
  file_path = sys.argv[1]

  # Variáveis de Registradores
  registers = Reg()
    
  # Variáveis da ULA
  ula = ULA()
  Zero = True
  NonZero = False

  # Variáveis de Memória
  mem = None
  mem_pos = 0
  inst_part = None

  if (file_path):
    bytes_inst = get_file_content(file_path)
    cs = Control_Storage(bytes_inst['bytes'], bytes_inst['size'])
    mem = cs.get_mem_of_instructions()

  while True:
    wait_for_clock()

    ####################################### PARTE 1: Decodificar #####################################
    inst = mem[mem_pos]
    inst_part = inst.get_inst_dict()
    
    ####################################### PARTE 2: Barramentos #####################################
    b = registers.get_register_b(inst_part['bus_b'])

    ####################################### PARTE 3: ULA #############################################

    ula.set_inputs(registers.get_register("h"), b)

    # Recebe instrucao da ula TEMPORARIO SERA FEITO NA PARTE 1
    instrucao = "10111100"
    ula.set_instruction(instrucao)

    ula.execute_instruction()

    if(ula.is_zero()): Zero = True
    if(not ula.is_zero()): Zero = False
    NonZero = not Zero

    ####################################### PARTE 4: Registradores ####################################

    # Recebe registrador para ser gravado, sendo ele representado pelos bits C
    C = "000000100"
    for i in range(0, len(C)):
      registers.set_register(i, ula.get_result())
        
    ####################################### PARTE 5: Memoria ##########################################

    ####################################### PARTE 6: Jumps ############################################

		####################################### PARTE 7: NEXT ADDRESS #####################################
    mem_pos	+= convert_to_decimal(inst_part['next_address'])

def wait_for_clock():
  """ Entrada: Nada
      Operacao: Pausa o programa ate que a tecla enter seja pressionada,
                utilizada para separar os ciclos do clock durante a execucao das instrucoes
      Saida: Nada """

  input("")

main()
