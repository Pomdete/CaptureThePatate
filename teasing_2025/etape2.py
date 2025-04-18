#!/usr/bin/env python3

def generate_local_50():
    """
    Reproduit l'algorithme de génération des premiers 24 octets du tableau local_50
    tel que défini dans la fonction verif.
    """
    local_50 = bytearray(80)  # Initialise un tableau de 80 octets à zéro
    
    # Initialisation du registre LFSR
    lfsr = 0x7F
    
    # La boucle principale qui s'exécute 0xC0 (192) fois
    i = 0
    while i < 0xC0:
        # Pour chaque bit dans un octet
        for j in range(8):
            # Calcul du feedback bit
            feedback = lfsr & 0x71  # Masque pour extraire certains bits
            
            # Calcul du bit de parité des bits extraits
            parity = feedback
            for k in range(1, 8):
                parity ^= (feedback >> k) & 0xFF
            
            # Mise à jour de local_50
            idx = i + 7 if i < 0 else i
            idx = idx >> 3  # Divise par 8 pour obtenir l'index de l'octet
            bit_pos = j  # Position du bit dans l'octet
            
            # XOR le bit dans local_50
            local_50[idx] ^= ((lfsr & 1) << bit_pos)
            
            # Mise à jour du LFSR
            lfsr = (lfsr >> 1) | ((parity & 1) << 7)
            
            i += 1
    
    return local_50[:24]  # Retourne les 24 premiers octets

def find_flag(first_24_bytes, known_data):
    """
    Trouve le flag en inversant l'opération XOR.
    
    La logique est:
    1. local_50[0:24] contient les premiers 24 octets générés
    2. local_50[24:48] contient known_data
    3. Le code fait: local_50[24:48] = local_50[0:24] ^ local_50[24:48]
    4. Puis vérifie que local_50[24] == 'F', local_50[25] == 'C', etc.
    5. Et enfin vérifie que local_50[24:48] == flag
    
    Donc flag = local_50[0:24] ^ known_data
    """
    flag = bytearray(24)
    for i in range(24):
        flag[i] = first_24_bytes[i] ^ known_data[i]
    
    return flag

def main():
    # Générer les 24 premiers octets de local_50
    first_24_bytes = generate_local_50()
    print("Premiers 24 octets générés:", ' '.join(f'{b:02x}' for b in first_24_bytes))
    
    # Données exactes de DAT_3f403840
    known_data = bytearray([
        0x39, 0x03, 0xb2, 0xef, 0xf8, 0x0e, 0x71, 0xb4,
        0xdb, 0x93, 0xf6, 0x51, 0x3a, 0x62, 0xa6, 0xe8,
        0x64, 0x9b, 0x81, 0x04, 0x01, 0x42, 0x74, 0xb5
    ])

    print("Données connues (DAT_3f403840):", ' '.join(f'{b:02x}' for b in known_data))
    
    # Trouver le flag
    flag_bytes = find_flag(first_24_bytes, known_data)
    print("Flag en bytes:", ' '.join(f'{b:02x}' for b in flag_bytes))
    
    # Vérifier que les 4 premiers caractères sont bien "FCSC"
    print("4 premiers caractères:", flag_bytes[:4].decode('ascii', errors='replace'))
    
    # Convertir en chaîne ASCII
    flag_str = ''.join(chr(b) if 32 <= b <= 126 else f'\\x{b:02x}' for b in flag_bytes)
    print("Flag:", flag_str)
    
    # Vérification supplémentaire
    intermediate = bytearray(24)
    for i in range(24):
        intermediate[i] = first_24_bytes[i] ^ known_data[i]
    
    print("Vérification - Flag attendu commence par FCSC:", intermediate[:4] == b'FCSC')

if __name__ == "__main__":
    main()