from instruction import Instruction

"""Uma classe que representa o Armazenamento de Controle de 512 bytes"""
class Control_Storage:
  def __init__(self, bytes_instruction, file_size=512):
    """Inicializa um objeto Armazenamento de Controle
    
    Keyword arguments:
    bytes_instruction -- instruções MIC-1 em bytes
    file_size -- tamanho do arquivo de instruções MIC-1
    """
    self.mem = [bytes_instruction[i:i+8] for i in range(0, file_size, 8)]

  def get_mem_of_bytes(self):
    """Retorna uma lista de instruções(64 bits) MIC-1 em bytes"""
    return self.mem

  def get_mem_of_instructions(self):
    """Retorna uma lista de objetos Instruction"""
    def define_instructions(elem):
      return Instruction(elem)

    instructions_map = map(define_instructions, self.mem)
    return list(instructions_map)

  def get_mem_of_str(self):
    """Retorna uma lista de instruções em string"""
    def define_str_instructions(elem):
      return elem.get_str_instruction()

    instruction_map = map(define_str_instructions, self.get_mem_of_instructions())
    return list(instruction_map)

  def get_mem_of_arr(self):
    """Retorna uma lista de lista de instruções"""
    def define_arr_instruction(elem):
      return elem.get_arr_instruction()
    
    instruction_map = map(define_arr_instruction, self.get_mem_of_instructions())
    return list(instruction_map)

    