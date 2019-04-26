class Reg:

    def __init__(self):
        """ Entrada: Nada
            Operacao: Inicia o objeto dos Registradores com todos os campos zerados, Construtor
            Saida: Objeto dos Registradores """
        #                 mar | mdr | pc | mbr | sp | lv | cpp | tos | opc | h
        self.registers = [ 0  ,  0  ,  0 ,  0  , 0  ,  0 ,  0  ,  0  ,  0  , 0]
    


    def get_register(self, register):
        """ Entrada: register: Inteiro ou String => Registrador a ser acessado
            Operacao: Acessa o registrador especificado
            Saida: Valor do registrador especificado: Inteiro """

        if(type(register) is int):
            return self.registers[register]

        if(type(register) is str):
            reg_names = ["mar", "mdr", "pc", "mbr" , "sp", "lv" , "cpp", "tos", "opc", "h"]
            return self.registers[reg_names.index(register)]


    def set_register(self, register, value):
        """ Entrada: register: Inteiro ou String => Registrador a ser editado
                     value: Inteiro => Valor a ser atribuido ao registrador
            Operacao: Altera o valor do registrador especificado
            Saida: Nada """
        
        if(type(register) is int):
            self.registers[register] = value

        if(type(register) is str):
            reg_names = ["mar", "mdr", "pc", "mbr" , "sp", "lv" , "cpp", "tos", "opc", "h"]
            self.registers[reg_names.index(register)] = value

            