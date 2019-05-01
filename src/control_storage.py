from instruction import Instruction
from reader import get_file_content

"""Uma classe que representa o Armazenamento de Controle de 512 bytes"""
class Control_Storage:
  def __init__(self):
    """Inicializa um objeto Armazenamento de Controle"""
    content_file = get_file_content("bin/microprog.rom")
    bytes_inst = content_file["bytes"]
    file_size = content_file["size"]

    self.cs_bytes = [bytes_inst[i:i+8] for i in range(0, file_size, 8)]
    self.cs_instructions = self._get_cs_of_instructions()

  def get_cs(self, cs_type="instructions"):
    """Retorna uma lista de instruções(64 bits) MIC-1 em bytes"""
    if (cs_type == "bytes"): return self.cs_bytes
    return self.cs_instructions

  def get_cs_value(self, position, cs_type="instructions"):
    if (cs_type == "bytes"): return self.cs_bytes[position]
    return self.cs_instructions[position]

  def _get_cs_of_instructions(self):
    """Retorna uma lista de objetos Instruction"""
    def define_instructions(elem):
      return Instruction(elem)

    instructions_map = map(define_instructions, self.cs_bytes)
    return list(instructions_map)

  def _get_cs_of_str(self):
    """Retorna uma lista de instruções em string"""
    def define_str_instructions(elem):
      return elem.get_str_instruction()

    instruction_map = map(define_str_instructions, self._get_cs_of_instructions())
    return list(instruction_map)

  def _get_cs_of_arr(self):
    """Retorna uma lista de lista de instruções"""
    def define_arr_instruction(elem):
      return elem.get_arr_instruction()
    
    instruction_map = map(define_arr_instruction, self._get_cs_of_instructions())
    return list(instruction_map)
