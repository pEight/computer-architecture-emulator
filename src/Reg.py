from binary import convert_to_decimal

class Reg:

  def __init__(self):
    """ Entrada: Nada
        Operacao: Inicia o objeto dos Registradores com todos os campos zerados, Construtor
        Saida: Objeto dos Registradores """

    self.dict = {
      "h": 0,
      "opc": 0,
      "tos": 0,
      "cpp": 0,
      "lv": 0,
      "sp": 0,
      "pc": 0,
      "mdr": 0,
      "mar": 0,
      "mbr": 0
    }

  def get_register(self, register):
    """ Entrada: register: String => Registrador a ser acessado
        Operacao: Acessa o registrador especificado
        Saida: Valor do registrador especificado: Inteiro """

    if(register == "none"): return 0

    return self.dict[register]

  def set_register(self, register, value):
    """ Entrada: register: String => Registrador a ser editado
                 value: Inteiro => Valor a ser atribuido ao registrador
        Operacao: Altera o valor do registrador especificado
        Saida: Nada """

    self.dict[register] = value

  def get_register_bin(self, register):
    """ Entrada: register: String => Parte binaria da instrucao em string
        Operacao: Retorna o regitrados especificado
        Saida: O valor registrador especificado """

    # inv_reg = register[::-1]
    index = register.index('1')

    names_array = self.dict.keys()

    return self.dict[names_array[index]]

  def set_register_bin(self, register, value):
    """ Entrada: register: String => Parte binaria da instrucao em string
                 value: Int => Valor a ser atribuido ao registrador
        Operacao: Altera o valor do registrador especificado
        Saida: Nada """

    # inv_reg = register[::-1]
    index = register.index('1')

    names_array = self.dict.keys()

    self.dict[names_array[index]] = value

  def get_register_name(self, register):
    """ Entrada: register: String => Parte binaria da instrucao em string
        Operacao: Retorna o nome do regitrados especificado
        Saida: O valor registrador especificado """

    index = convert_to_decimal(register)

    reg_names = ["none", "h", "opc", "tos", "cpp", "lv", "sp", "pc", "mdr", "mar", "mbr"]

    return reg_names[index]

  def get_register_b(self, register):
    """ Entrada: register: String => Parte binaria que representa qual sera o barramento b
        Operacao: Retorna o nome do regitrador especificado
        Saida: O nome do registrador especificado """

    # Pelo que vi, a string não está adequada para ser convertida desse modo
    # Portanto ela precisa ser invertida
    inv_reg = register[::-1]

    intRegister = convert_to_decimal(inv_reg)

    reg_names_for_b = ["mdr", "pc", "mbr", "mbr", "sp", "lv", "cpp", "tos", "opc"]

    reg_value = self.dict[reg_names_for_b[intRegister]]

    if(intRegister == 2 and reg_value & (0b10000000)):
      reg_value = reg_value | (0b111111111111111111111111 << 8)

    return reg_value
