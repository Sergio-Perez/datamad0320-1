import random
import os 
import sys
from argparse import ArgumentParser
import subprocess

def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])
    #return proc.stdout.read()

def saluda(lang,lugar):
    ta = random.choice(["Felipe","Clara","Marc"])
    if lang=="es":
        return f"Hola {ta} desde {lugar}"
    elif lang=="en":
        return f"Hello {ta} from {lugar}"
    else:
        return "No puedo saludar"


parser = ArgumentParser(description="Este programa es para saludar a los TA")

parser.add_argument("--lang",help="el idioma con el que saludar", default="es")
parser.add_argument("--lugar",help="desde donde saludar", default="la playa")
parser.add_argument("--times",help="veces que saludar", default=1, type=int)
parser.add_argument("--say",help="dilo en voz alta", action='store_true')

args = parser.parse_args()
#print(args)

result = []
for i in range(args.times):
    result.append(saluda(args.lang,args.lugar))

saludototal = '\n'.join(result)
if args.say:
    print(saludototal)
    voices = ["Alex","Amelie","Fiona","Kyoko","Luciana","Monica"]
    selected_voice = random.choice(voices)

    print(f"Now the voice of {selected_voice}!")
    cmd = f"say -v '{selected_voice}' '{saludototal}'"
    print(cmd)
    bash_command(cmd)
else:
    print(saludototal)
