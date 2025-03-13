from pwn import *

# Paramètres de connexion
HOST, PORT = "localhost", 4000

def comparer(x, y):
	io.sendlineafter(b">>> ", f"comparer {x} {y}".encode())
	return int(io.recvline().strip().decode())

def echanger(x, y):
	io.sendlineafter(b">>> ", f"echanger {x} {y}".encode())

def longueur():
	io.sendlineafter(b">>> ", b"longueur")
	return int(io.recvline().strip().decode())

def verifier():
	io.sendlineafter(b">>> ", b"verifier")
	r = io.recvline().strip().decode()
	if "flag" in r:
		print(r)
	else:
		print(io.recvline().strip().decode())
		print(io.recvline().strip().decode())

def trier(N):
	for i in range(N):
		for j in range(i + 1, N):
			if not comparer(i, j):
				echanger(i, j)
	pass

# Ouvre la connexion au serveur
io = remote(HOST, PORT)
print("Connexion établie")
# Récupère la longueur du tableau
N = longueur()
print(f"Longueur du tableau : {N}")
# Appel de la fonction de tri que vous devez écrire
trier(N)

# Verification
verifier()

# Fermeture de la connexion
io.close()
