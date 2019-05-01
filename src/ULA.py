class ULA:

    def __init__(self):
        """ Entrada: Nada
            Operacao: Inicia o objeto da ULA com campos zerados, Construtor
            Saida: Objeto da ULA """

        self.a = 0
        self.b = 0
        self.inst = 0
        self.result = 0
    

    def set_instruction(self, inst):
        """ Entrada: inst: String => Instrucao a ser executada pela ULA
            Operacao: Atribui ao campo de instrucao da ula a sua nova instrucao passada como parametro
                      Realiza a separacao da instrucao e dos bits de deslocamento
            Saida: Nada """
        
        self.shift = inst[:2]
        self.inst = inst[2:]


    def set_inputs(self, a, b):
        
        """ Entrada: a , b: Inteiros => Valores dos registradores H e B
            Operacao: Atribui aos campos a e b da ULA os valores recebidos
            Saida: Nada """ 
        
        self.a = a # Receber o valor do registrador h
        self.b = b # Recebe o valor de um registrador baseado no B
    

    def execute_instruction(self):
        """ Entrada: Nada
            Operacao: Executa a instrucao passada para a ula atraves de setInstruction
            Saida: Resultado da operacao executada pela ula """
        
        # Todas as istrucoes da ULA
        instructions = ["011000", "010100", "011010", "101100", "111100", "111101", "111001", "110101", "111111", "110110", "111011", "001100", "011100", "010000", "110001","110010"]
        # Os resultados relacionados a cada instrucao 
        results = [self.a, self.b, ~ self.a, ~ self.b, self.a + self.b, self.a + self.b + 1, self.a + 1, self.b + 1, self.b - self.a, self.b - 1, -1*self.a, self.a & self.b, self.a | self.b , 0, 1, -1 ]

        self.result = results[ instructions.index(self.inst) ]

        return self.result

    def execute_shift(self):
        """ Entrada: Nada
            Operacao: Executa os deslocamentos para da direita ou esquerda se necessário
            Saida: Resultado da operacao executada pela ula após o deslocamento """
        if(self.shift == "01"):
            self.result = self.result >> 1
        if(self.shift == "10"):
            self.result = self.result << 8

    def is_zero(self):
        """ Entrada: Nada
            Operacao: Verifica se a ula tem resultado zero
            Saida: Boolean: True se a ula tiver valor zero, falso se tiver valor diferente de zero """
        return self.result == 0

    def get_result(self):
        """ Entrada: Nada
            Operacao: Retorna o resultado da ula
            Saida: Int: Resultado da ula """
        return self.result
