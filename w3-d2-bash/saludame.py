import random
import os 
import sys

def saluda(lang,lugar):
    ta = random.choice(["Felipe","Clara","Marc"])
    if lang=="es":
        print(f"Hola {ta} desde {lugar}")
    elif lang=="en":
        print(f"Hello {ta} from {lugar}")
    else:
        print("No puedo saludar")


print(sys.argv)

# Parametrize this program with the "LUGAR" environment variable
lugar = os.getenv("LUGAR")

# Read the lang flag
lang = sys.argv[2]
saluda(lang,lugar)