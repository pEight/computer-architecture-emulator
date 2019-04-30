class Reg:

    def __init__(self):
        """ Entrada: Nada
            Operacao: Inicia o objeto dos Registradores com todos os campos zerados, Construtor
            Saida: Objeto dos Registradores """
        #                  h |  opc | tos | cpp | lv | sp | pc | mdr | mar | mbr
        self.registers = [ 0  ,  0  ,  0 ,  0  , 0  ,  0 ,  0  ,  0  ,  0  , 0]
    


    def get_register(self, register):
        """ Entrada: register: Inteiro ou String => Registrador a ser acessado
            Operacao: Acessa o registrador especificado
            Saida: Valor do registrador especificado: Inteiro """

        if(type(register) is int):
            return self.registers[register]

        if(type(register) is str):
            if(register == "none"): return 0
            reg_names = ["h", "opc", "tos", "cpp" , "lv", "sp" , "pc", "mdr", "mar", "mbr"]
            return self.registers[reg_names.index(register)]


    def set_register(self, register, value):
        """ Entrada: register: Inteiro ou String => Registrador a ser editado
                     value: Inteiro => Valor a ser atribuido ao registrador
            Operacao: Altera o valor do registrador especificado
            Saida: Nada """
        
        if(type(register) is int):
            self.registers[register] = value

        if(type(register) is str):
            reg_names = ["h", "opc", "tos", "cpp" , "lv", "sp" , "pc", "mdr", "mar", "mbr"]
            self.registers[reg_names.index(register)] = value

    def get_register_bin(self, register):
        """ Entrada: register: String => Parte binaria da instrucao em string
            Operacao: Retorna o regitrados especificado
            Saida: O valor registrador especificado """

        # inv_reg = register[::-1]
        index = register.index('1')
        return self.registers[index]

    def set_register_bin(self, register, value):
        """ Entrada: register: String => Parte binaria da instrucao em string
                     value: Int => Valor a ser atribuido ao registrador
            Operacao: Altera o valor do registrador especificado
            Saida: Nada """

        # inv_reg = register[::-1]
        index = register.index('1')
        self.registers[index] = value

    def get_register_name(self, register):
        """ Entrada: register: String => Parte binaria da instrucao em string
            Operacao: Retorna o nome do regitrados especificado
            Saida: O valor registrador especificado """

        # inv_reg = register[::-1]
        
        if register == "0000": return 'none'
        index = register.index('1')
        reg_names = ["h", "opc", "tos", "cpp" , "lv", "sp" , "pc", "mdr", "mar", "mbr"]
        return reg_names[index]