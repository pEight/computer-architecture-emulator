# Arquivo principal
# Responsável por chamar todas as outras funcoes e dar inicio ao programa

import sys

from Reg import Reg
from ULA import ULA

from binary import convert_to_decimal
from control_storage import Control_Storage
from instruction import Instruction


def main():
  # Variáveis de Registradores
  registers = Reg()

  # Variáveis da ULA
  ula = ULA()
  Zero = True
  NonZero = False

  # Variáveis de armazenamento de controle
  cs = Control_Storage()
  cs_pos = 0
  instruction_part = None

  while True:
    wait_for_clock()

    ####################################### PARTE 1: Decodificar #####################################
    instruction = cs.get_cs_value(cs_pos)
    instruction_part = instruction.get_inst_dict()

    ####################################### PARTE 2: Barramentos #####################################
    b = registers.get_register_b(instruction_part['bus_b'])

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
    cs_pos = convert_to_decimal(instruction_part["next_address"])


def wait_for_clock():
  """ Entrada: Nada
      Operacao: Pausa o programa ate que a tecla enter seja pressionada,
                utilizada para separar os ciclos do clock durante a execucao das instrucoes
      Saida: Nada """

  input("")


main()
