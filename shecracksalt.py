#!/usr/bin/python3
from hashlib import sha1
import base64
from tqdm import tqdm
import os

def mostrar_banner():
    print("""
    ███████╗██╗  ██╗ █████╗     ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
    ██╔════╝██║  ██║██╔══██╗   ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
    ███████╗███████║███████║   ██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██║  ██║
    ╚════██║██╔══██║██╔══██║   ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██║  ██║
    ███████║██║  ██║██║  ██║██╗╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██████╔╝
    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ 
    """)

def generar_hash(salt, password):
    hash_obj = sha1()
    hash_obj.update(salt.encode('utf-8'))
    hash_obj.update(password.encode('utf-8'))
    hashed_bytes = hash_obj.digest()
    return f"$SHA1${salt}${base64.urlsafe_b64encode(hashed_bytes).decode('utf-8').replace('+', '.')}"

def buscar_contraseña(salt, target_hash, wordlist):
    try:
        with open(wordlist, 'r', encoding='latin-1', errors='ignore') as f:
            total = sum(1 for _ in f)
            f.seek(0)
            
            for line in tqdm(f, total=total, desc="Probando contraseñas", unit="pwd"):
                password = line.strip()
                if generar_hash(salt, password) == target_hash:
                    return password
        return None
    except FileNotFoundError:
        print(f"\n[-] Error: No se encontró el archivo {wordlist}")
        return None

def main():
    mostrar_banner()
    
    print("\n[+] Modos de operación:")
    print("1. Buscar un hash individual")
    print("2. Buscar múltiples hashes desde archivo")
    opcion = input("\nSeleccione el modo (1/2): ").strip()
    
    # Configuración común
    salt = input("\nIngrese el salt (por ejemplo 'd'): ").strip()
    wordlist = input("Ruta a la wordlist (ej. rockyou.txt): ").strip()
    
    if opcion == "1":
        # Modo hash individual
        target_hash = input("Ingrese el hash completo a descifrar: ").strip()
        print(f"\n[+] Buscando contraseña para hash: {target_hash}")
        print(f"[+] Usando salt: '{salt}' y wordlist: {wordlist}\n")
        
        password = buscar_contraseña(salt, target_hash, wordlist)
        if password:
            print(f"\n[+] ¡CONTRASEÑA ENCONTRADA!: {password}")
        else:
            print("\n[-] Contraseña no encontrada en la wordlist")
    
    elif opcion == "2":
        # Modo múltiples hashes
        hash_file = input("Ruta al archivo con hashes (uno por línea): ").strip()
        
        if not os.path.isfile(hash_file):
            print(f"\n[-] Error: No se encontró el archivo {hash_file}")
            return
        
        with open(hash_file, 'r') as f:
            hashes = [line.strip() for line in f if line.strip()]
        
        print(f"\n[+] Buscando contraseñas para {len(hashes)} hashes")
        print(f"[+] Usando salt: '{salt}' y wordlist: {wordlist}\n")
        
        encontradas = 0
        for target_hash in hashes:
            password = buscar_contraseña(salt, target_hash, wordlist)
            if password:
                print(f"\n[+] Hash: {target_hash}")
                print(f"[+] Contraseña: {password}")
                encontradas += 1
        
        print(f"\n[+] Proceso completado. Se encontraron {encontradas}/{len(hashes)} contraseñas")
    
    else:
        print("\n[-] Opción no válida. Debe seleccionar 1 o 2")

if __name__ == '__main__':
    main()
