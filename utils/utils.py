import os

# --------- Limpiar la consola ---------

def clearConsole():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)