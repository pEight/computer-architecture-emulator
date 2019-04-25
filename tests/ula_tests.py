# Função de teste da ULA

#Importando o arquivo de /src
import sys
sys.path.insert(0, '../src')
from ULA import ULA

minhaUla = ULA()
minhaUla.setInputs()
minhaUla.setInstruction(60)

instructions = [24, 20, 26, 44, 60, 61, 57, 53, 63, 54, 59, 12, 28, 16, 49, 50]

for i in instructions:
    minhaUla.setInstruction(i)
    print(minhaUla.executeInstruction())