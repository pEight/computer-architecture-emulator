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
        """ Entrada: inst: Inteiro => Instrucao a ser executada pela ULA
            Operacao: Atribui ao campo de instrucao da ula a sua nova instrucao passada como parametro
            Saida: Nada """
        
        self.inst = inst
    

    def set_inputs(self):
        """ Entrada: Nada
            Operacao: Chama as funcoes de acesso ao registrador e atribui aos campos a e b da ULA
            Saida: Nada """ 
        

        # Essa funcao depois ira acessar o valor dos registradores
        self.a = 12 # Receber o valor do registrador h
        self.b = 10 # Recebe o valor de um registrador baseado no B
    

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