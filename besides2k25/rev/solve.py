import struct

# ELF file 

#The challenge is a simple vm that performs basic operations on matrix like add sub xor mul swap_col and swap_row
#we just need to perform the operations  on the reverse order and only instructions that need one matrix 

# the vm instructions 
#swap column with 4 bytes : 0x30  [target matrix : in this case the given matrix] [row_1] [row_2]
#swap row with 4 bytes also : 0x40 [target matrix] [col_1] [col_2]
#no need to specify other instructions

#note: it stays the same if u reverse the order between rows or cols 

#scrambled flag 
#we extract the flag scrambled as a matrix in the given matrix.txt
matrix = [
    [115,123,104,51,101,108,115,108],
    [51,104,95,109,95,52,116,116],
    [116,52,114,49,95,120,109,95],
    [102,48,95,114,104,51,95,118],
    [108,101,108,109,115,97,104,116],
    [114,48,108,100,95,33,119,125],
    [95,116,104,52,51,99,51,107],
    [56,95,120,56,118,95,77,108]
]

#we extract the vm instructions  using xxd program.bin 
bytecode_hex = (
    "40000003300000054000010430000106"
    "40000205300002074000030630000300"
    "40000407300004018000015000027000"
    "03600004800005400002063000010750"
    "00016000038000024000070030000702"
    "80000160000540000601300006038000"
    "02600005400005023000050480000360"
    "00057000045000034000040530000306"
    "800001600002500005cc00"
)

def parse_instructions(hex_str):
    raw = bytes.fromhex(hex_str)
    instrs = []
    pc = 0 #program counter like rip in registers so we can jump over instructions , 0 at the begining ( start of the program.bin)
    while pc < len(raw):
        op = raw[pc] # extract the opcode from the instruction
        if op in [0x30, 0x40]: 
            instrs.append((op, raw[pc+1:pc+4]))
            pc += 4
        elif op in [0x50, 0x60, 0x70, 0x80]: #opcodes of add , sub ..  
           # instrs.append((op, raw[pc+1:pc+3])) # we don't need to add them to the map because we will not execute them .
            pc += 3
        elif op == 0xCC: #print the matrix
            instrs.append((op, raw[pc+1:pc+2]))
            pc += 2
        else :
            print('do nothing') #unreachable
    return instrs

instructions = parse_instructions(bytecode_hex)

#start from the end of the vm -> start and skip the instructions that modify the ascci like add sub  .. because we don't need to modify them
#we just need to reorder them
for op, args in reversed(instructions):
    if op == 0x40: # the opcode of swapping rows , u can inspect it  in the decompilation code at the end ( the switch case ) 
        r1, r2 = args[1], args[2]
        matrix[r1], matrix[r2] = matrix[r2], matrix[r1]
        
    elif op == 0x30: # the opcode of swapping cols 
        c1, c2 = args[1], args[2]
        for r in range(8):
            matrix[r][c1], matrix[r][c2] = matrix[r][c2], matrix[r][c1]
            

for row in matrix:
    line = "".join(chr(c % 256) for c in row) 
    print(line,end="")# we print the flag here mod 256 to be on the range of (0,255)
print('\n')
