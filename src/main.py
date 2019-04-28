import os
from instruction import Instruction
from control_storage import Control_Storage

bin_path = 'bin/microprog.rom'

def get_binary_content(filename, chunksize):
  with open(filename, mode='rb') as f:
    byte = f.read(chunksize)

    if byte:
      return byte
    
    return None

file_size = os.path.getsize(bin_path)
bytes_instruction = get_binary_content(bin_path, file_size)

mem_test = Control_Storage(bytes_instruction, file_size)

# print(mem_test.get_mem_of_instructions())
# print(mem_test.get_mem_of_str())
# print(mem_test.get_mem_of_arr())

mem_test = mem_test.get_mem_of_instructions()

inst = mem_test[0]

print(f'Instruction string: {inst.get_str_instruction()}')
print(f'Instruction Arr: {inst.get_arr_instruction()}')
print(f'Bus B: {inst.get_bus_b_bin()}')
print(f'Memória: {inst.get_memory_bin()}')
print(f'Bus C: {inst.get_bus_c_bin()}')
print(f'ULA: {inst.get_ula_bin()}')
print(f'JAM: {inst.get_jam_bin()}')
print(f'Next Address: {inst.get_next_address_bin()}')


# INIC        || CPP         || LV          || PC 
# 00 73 00 00 || 06 00 00 00 || 01 10 00 00 || 00 04 00 00
# constante na inicialização
# apenas muda o topo da pilha

