# Commands
* `<command> --help` Ver ayuda
* `man <command>` Ver ayuda
* `wc -l` cuenta lineas de stdout
* `grep` filtra stdout
* `cut` recorta stdout por filas y campos
* `sort` ordena los resultados de stdout

# Basic bash commands with pipe operator`|`
* Muestra 10 primeras lineas de un fichero: `cat vehicles_limpio.csv | head`
* De un csv, muestra los 10 primeros valores de la columna 3 `cat vehicles_limpio.csv | cut -d "," -f3 | head`
* Lo mismo que el anterior pero guardando el resultado en un fichero `cat vehicles_limpio.csv | cut -d "," -f2 -f3 | head > datoslimpios.csv`

# Operations
* Cuenta todos los Audi: `cat data/vehicles_limpio.csv | cut -d "," -f2 -f3 | grep "Audi" | wc -l`
* Cuenta todos los Audi y elimina repetidos : `cat data/vehicles_limpio.csv | cut -d "," -f2 -f3 | grep "Audi" | sort | uniq`

# Environment variables
* `echo $PATH` is the system variable that the terminal uses to find programs
* Export an environment variable to be used in all programs in terminal `export PEPE=33`
* Print the contents of variable `echo $PEPE`