global counter, accumulator

memory = [0] * 32
counter = 0
register = 0
accumulator = 0

naccr =  [0, 1, 26, 27, 28, 29, 30, 31]

def instruction_to_function(instruction, i):

    register = i

    switcher = {'ADD': Add,
    'NOT':Not,
    'ADDI':Add,
    'AND':And,
    'ORR':Or,
    'DIV':Div,
    'MUL':Mul,
    'SUB':Sub,
    'XOR':Xor,
    'LSL':Lsl,
    'LSR':Lsr,
    'NEG':Neg,
    'STR':Str,
    'LDI':Ldi,
    'LDM':Ldm,
    'BRN':Brn,
    'BRZ':Brz }

    invoke_function = switcher.get(instruction)
    invoke_function(register)


class simulator(object):

    symbol_table = {}
    current_location = 0
    default_mem_loc  = 0
    instruction_table = {}
    register_table = {}

    def __init__(self, default_memory_location, instruction_table):

        self.default_mem_loc    = default_memory_location
        self.instruction_table  = instruction_table

    def first_pass(self, lines):

        self.current_location = self.default_mem_loc

        for line in lines:
            if not len(line):
                continue
            self.current_location += 1
            #print("current location", self.current_location)

    def second_pass(self, lines):


        self.current_location = self.default_mem_loc
        i = 0
        while i < len(lines):

            #print(len(lines))
            line = lines[i]
            #print("line is :", line)
            instruction = line[0:line.find(' ')].strip()
            inputs        = line[line.find(' ') + 1:].replace(' ', '').split(',')
            #print("instruction : ", instruction)
            #print("inputs : ", inputs)
            #print("second pass location : ",self.current_location )

            if not instruction:
                break

            j = i
            status = True
            while status:
                global counter
                print("\nDo you want to check\n")
                ans = input()
                if ans == 'y' or ans =='Y':
                    if instruction in self.instruction_table.keys():
                        i = self.parse_instruction(instruction, inputs, j)
                        print("The value in the accumulator is :", accumulator)
                        print("The value in the memory  is :", memory)

                    else:
                        print("INSTRUCTION:" + instruction + "IS INVALID! ABORT")
                        exit()
                status = False

            counter += 1

    def parse_instruction(self, instruction, input_args, i):

        instruction_type = self.instruction_table[instruction]
        j = i
        args = input_args[:]
        #print("args is :", args)
        if instruction_type == "i":
            rt  = int(args[0])
            #print("type of rt is :", type(rt))

            if len(args) == 1:
    
                    if not rt in naccr:
                        instruction_to_function(instruction, rt)
                    return int(j + 1)
            else:
                imm = int(args[0])
                if not rt in naccr:
                    pass
                return int(j+1)
        else:
            print("Son else ")
            rv = int(args[0][:-1])
            return rv

# Functions


def Add(a):
    global accumulator,counter
    accumulator = accumulator + memory[a]
    counter += 1

def Sub(a):
    global accumulator,counter
    accumulator = accumulator - memory[a]
    counter += 1

    
def And(a):
    global accumulator,counter
    accumulator = accumulator & memory[a]
    counter += 1

def Or(a):
    global accumulator,counter
    accumulator = accumulator | memory[a]
    counter += 1

def Div(a):
    global accumulator,counter
    accumulator = accumulator / memory[a]
    counter += 1

def Mul(a):
    global accumulator,counter
    accumulator = accumulator * memory[a]
    counter += 1

def Xor(a):
    global accumulator,counter
    accumulator = accumulator ^ memory[a]
    counter += 1

def Lsr(a):
    global accumulator,counter
    accumulator = accumulator >> a 
    counter += 1

def Lsl(a):
    global accumulator,counter
    accumulator = accumulator << a 
    counter += 1

def Neg(a):
    global accumulator,counter
    accumulator = -accumulator
    counter += 1

def Str(a):
    global accumulator,counter
    memory[a] = accumulator
    counter += 1

def Ldm(a):
    global accumulator,counter
    accumulator = memory[a]
    counter += 1

def Ldi(a):
    global accumulator,counter
    accumulator = a
    counter += 1

def Brn(a):
    counter = counter + a
    counter += 1

def Brz(a):
    counter = counter + a
    counter += 1


def Not(a):
    global accumulator,counter
    accumulator = ~accumulator
    counter += 1

