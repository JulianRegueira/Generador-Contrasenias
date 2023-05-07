import random
import string

def generar_contrasena(longitud):
    # Establecer caracteres a utilizar en la contraseña
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Generar contraseña aleatoria
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    
    return contrasena

# Se le asigna la longitud deseada de la contraseña a crear
contrasena = generar_contrasena(10)
print(contrasena)