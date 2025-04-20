# 🔐 Password Hash Cracker (Python Script)

💡 como usar:

    python3 shecracksalt.py
    
Este script en Python está diseñado para descifrar contraseñas a partir de hashes utilizando ataques de diccionario (wordlist). 
Soporta tanto hashes individuales como listas de hashes desde archivos.
🛠️ Características

- Compatible con múltiples algoritmos de hash (SHA1, SHA256, MD5, etc.)

- Soporte para salt estático o dinámico

- Procesamiento en paralelo para mayor velocidad

   ## Modos de uso:

- Hash único (-hash)
- Archivo de hashes (-hashfile)
- Wordlist personalizada (-wordlist)

## 🔍 Conceptos Clave

� ¿Qué es un hash?

Función criptográfica unidireccional que transforma datos (ej. contraseñas) en una cadena de longitud fija. Ejemplo:
# SHA1 de "password":
"5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8"

🧂 ¿Qué es un salt?

Cadena aleatoria añadida a la contraseña antes de hashear para prevenir:

- Ataques con tablas rainbow

- Colisiones en hashes idénticos

Ejemplo con salt:

          Contraseña: "secret", Salt: "abc"
          hash("abc" + "secret") → "1bd71c..."

📜 Base64 en Hashes

Los hashes se codifican en Base64 para:
- Representación segura en ASCII
- Facilitar almacenamiento/transmisión
- Evitar problemas con caracteres binarios
