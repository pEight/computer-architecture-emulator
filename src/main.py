# Arquivo principal
# Responsável por chamar todas as outras funcoes e dar inicio ao programa




def main():
    print("Hello World!")    
    memory = assign_memory();
    print(memory[0])
    print(memory[511])


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