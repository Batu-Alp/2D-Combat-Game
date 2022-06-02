import sys

code = [] 
machine_code = [] 

labels = {} 
symbols = {} 
opcodes_table = {} 
actual_table = {}

ısa_opcodes = ['LDI','LDM','NOT','ADD','SUB','BRZ','BRN', 'NEG','LSL', 'LSR', 'MUL', 'DIV', 'STR', 'XOR', 'ORR']

def Opcode(opcode, opcodeBin, instructionClass):
  if list(opcodes_table.keys()).count(opcode) == 0:
    opcodes_table[opcode] = [opcodeBin, instructionClass]

def Instructions(lineNum,line):

  opcodes = line.upper().split()

  if opcodes.count('LDI') == 1:
    Opcode('LDI','0010',1)
  elif opcodes.count('LDM') == 1:
    Opcode('LDM','0011',1)
  elif opcodes.count('NOT') == 1:
    Opcode('NOT','1101',1)
  elif opcodes.count('ADD') == 1:
    Opcode('ADD','0101',1)
  elif opcodes.count('SUB') == 1:
    Opcode('SUB','0110',1)
  elif opcodes.count('BRZ') == 1:
    Opcode('BRZ','0000',1)
  elif opcodes.count('BRN') == 1:
    Opcode('BRN','0001',1)
  elif opcodes.count('NEG') == 1:
    Opcode('NEG','1001',1)
  elif opcodes.count('LSL') == 1:
    Opcode('LSL','1010',1)
  elif opcodes.count('LSR') == 1:
    Opcode('LSR','1011',1)
  elif opcodes.count('MUL') == 1:
    Opcode('MUL','0111',1)
  elif opcodes.count('DIV') == 1:
    Opcode('DIV','1000',1)
  elif opcodes.count('STR') == 1:
    Opcode('STR','0100',1)
  elif opcodes.count('XOR') == 1:
    Opcode('XOR','1100',1)
  elif opcodes.count('ORR') == 1:
    Opcode('ORR','1100',1)
  else:
    print("Wrong Opcode")
    

def passOne():
  
  location_counter = 0
  simple_code = []

  for line_num, line in code:

    simple_code.append([line_num, line])
    Instructions(line_num, line)
    location_counter += 12

  return simple_code


def passTwo():
  for lineNum, line in code:
    split_lines = line.split()

    if split_lines[0] in opcodes_table.keys():
      temp=opcodes_table[split_lines[0]]
      machine_code.append(temp[0])

      if(temp[1] == 1):
        if( len(split_lines) == 2):
          if(split_lines[1] in symbols.keys()):
            addr = bin(symbols[split_lines[1]][1])[2:]
            while(len(addr)<8):
              addr = '0' + addr
            machine_code[-1] += addr

          elif(split_lines[1] in labels.keys()):
            addr = bin(labels[split_lines[1]])[2:]
            while(len(addr)<8):
              addr = '0' + addr
            machine_code[-1] += addr

          elif (split_lines[1] in actual_table.keys()):
            addr = bin(actual_table[split_lines[1]][1])[2:]
            while(len(addr)<8):
              addr='0'+addr
            machine_code[-1]+=addr

          elif(split_lines[1].isnumeric()):
            addr = bin(int(split_lines[1]))[2:]
            while(len(addr)<8):
              addr= '0' + addr
            machine_code[-1] += addr
 
     
      if(temp[1] == 0):
        machine_code[-1] += '00000000'
        if(len(split_lines)>1):
          print("Too many operand")

    else:
      print("Wron Opcode")
      pass
  file=open("bin.txt","w+")


  for i in machine_code:
    hex_code = binToHex(i[:4]) + binToHex(i[4:8]) + binToHex(i[4:8]) + binToHex(i[8:])
    file.write(hex_code + "\n")

     
  file.close()

def binToHex(arr):

  switcher = {	'0000':"0",
		'0001':"1",
		'0010':"2",
		'0011':"3",
		'0100':"4",
		'0101':"5",
		'0110':"6",
		'0111':"7",
		'1000':"8",
		'1001':"9",
		'1010':"A",
		'1011':"B",
		'1100':"C",
		'1101':"D",
		'1110':"E",
		'1111':"F"	
    }
    
  hex_num = switcher.get(arr)
  return hex_num


status = False
i = 0
for line in sys.stdin:
  i += 1
  if not line.strip():
    continue
  line = line.strip()
  code.append([i, line.strip()])
  if status:
    check = False
    for j in ısa_opcodes[:-1]:
      if line.upper().find(j) != -1:
        check = True
        break


code = passOne()
passTwo()
