from binary import convert_to_bin

"""Uma classe que representa uma instrução de 8 bytes(64 bits) MIC-1"""

class Instruction:
  def __init__(self, instruction_byte):
    """Inicializa atributos da instrução MIC-1
    
    Keyword arguments:
    instruction_byte -- Uma instrução de 8 bytes(64 bits)
    """
    self.instruction_byte = instruction_byte
    self.instruction_str = self._define_str_instruction()
    self.instruction_arr = self._define_arr_instruction()

  def _define_str_instruction(self):
    """Define uma string representando a instrução de 8 bytes em binário"""
    instruction_str = ""

    for byte in self.instruction_byte:
      bin_dict = convert_to_bin(byte)
      instruction_str += bin_dict['bin_str']

    return instruction_str

  def get_str_instruction(self):
    """Retorna uma string representando uma instrução de 8 bytes em binário"""
    return self.instruction_str

  def _define_arr_instruction(self):
    """Retorna uma lista de 0 e 1 representando uma instrução de 8 bytes em binário"""
    instruction_arr = []

    for byte in self.instruction_byte:
      bin_dic = convert_to_bin(byte)
      instruction_arr += bin_dic['bin_arr']

    return instruction_arr

  def get_arr_instruction(self):
    """Retorna a instrução MIC-1 como uma lista de 0 e 1"""
    return self.instruction_arr

  def get_byte_instruction(self):
    """Retorna a instrução MIC-1 como um tipo byte"""
    return self.instruction_byte

  def get_bus_b_bin(self):
    """Retorna a parte da instrução correspondente ao barramento B"""
    return self.instruction_str[:4]

  def get_memory_bin(self):
    """Retorna a parte da instrução correspondente a ação memória(write, read, fetch)"""
    return self.instruction_str[4:7]

  def get_bus_c_bin(self):
    """Retorna a parte da instrução correspondente ao barramento C"""
    return self.instruction_str[7:16]

  def get_ula_bin(self):
    """Retorna a parte da instrução correspondente a ULA"""
    return self.instruction_str[16:24]

  def get_jam_bin(self):
    """Retorna a parte da instrução correspondente ao JAM(JMPC, JAMN, JAMZ)"""
    return self.instruction_str[24:27]

  def get_next_address_bin(self):
    """Retorna a parte da instrução correspondente ao próximo endereço"""
    return self.instruction_str[27:36]

  def get_dict_instruction(self):
    """Retorna um Dictionary com barramento b, memória, barramento c,
    ULA e próximo endereço"""
    return {
      'bus_b': self.get_bus_b_bin(),
      'memory': self.get_memory_bin(),
      'bus_c': self.get_bus_c_bin(),
      'ula': self.get_ula_bin(),
      'jam': self.get_jam_bin(),
      'next_address': self.get_next_address_bin()
    }
