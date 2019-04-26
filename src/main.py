# Arquivo principal
# Responsável por chamar todas as outras funcoes e dar inicio ao programa

from Reg import Reg


def main():
    reg = Reg()
    
    reg.set_register("pc", 1042)
    print(reg.get_register("pc"))

    print("Hello World!")    
    memory = assign_memory();

    # Variavel que guarda o indice da instrucao atual a ser executada    
    current_position = 0
    
    while True:
        # current_inst = Instruction(memory[current_position])
        print(pc)
        pc = pc + 1
        wait_for_clock()


def assign_memory():
    """ Entrada: Nada
        Operacao: Cria o vetor da memoria e preenche suas posicoes com instrucoes
        Saida: Lista com as 512 posicoes de memoria inicializadas """

    memory = []

    #Trocar pela leitura do arquivo e iretacao das instrucoes
    for i in range(0, 512):
        memory.append("000000000000000000000000000000000000")

    return memory


def wait_for_clock():
    """ Entrada: Nada
        Operacao: Pausa o programa ate que a tecla enter seja pressionada,
              utilizada para separar os ciclos do clock durante a execucao das instrucoes
        Saida: Nada """

    input("")

main()