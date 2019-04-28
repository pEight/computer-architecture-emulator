# Arquivo principal
# Responsável por chamar todas as outras funcoes e dar inicio ao programa

from Reg import Reg
from ULA import ULA

def main():

    registers = Reg()
    
    ula = ULA()
    Zero = True
    NonZero = False

    while True:

        ####################################### PARTE 1: Decodificar #####################################

        ####################################### PARTE 2: Barramentos #####################################

        ####################################### PARTE 3: ULA #############################################

        # Recebe registrador que será adicionado ao b TEMPORARIO SERA FEITO NA PARTE 2
        b = "pc"
        ula.set_inputs(registers.get_register("h"), registers.get_register(b))

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
        registers.set_register(C.index(1), ula.get_result())
        
        ####################################### PARTE 5: Memoria ##########################################
        

        ####################################### PARTE 6: Jumps ############################################
        

def wait_for_clock():
    """ Entrada: Nada
        Operacao: Pausa o programa ate que a tecla enter seja pressionada,
              utilizada para separar os ciclos do clock durante a execucao das instrucoes
        Saida: Nada """

    input("")

main()