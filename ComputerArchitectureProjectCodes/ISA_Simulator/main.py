from isa_simulator import simulator
from instruction_table import instruction_table

print("ISA Simulator.\n")
print("Please enter the path.\n")

path = input()

asm = open(path, "r")
lines = asm.readlines()
print("Lines in the file : " , lines)
tool = simulator(0, instruction_table)
tool.first_pass(lines)
tool.second_pass(lines)


