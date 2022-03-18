import os
from login import login
from bienvenido import bienvenido
from registro import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database_boom.db")

print("Quiere  registrarse presione  1: \n"
       "Quiere iniciar sesion presione 2:")
opcion =int(input("Ingrese la opcion: "))

if opcion==1:
    insert_registro()
if opcion==2:
    login()
else:
    print("Opción Invalida")

#insert_registro()
#select_registro()
#insert_shots()
#insert_snaks()
#select_shots()
#select_snacks()
#login()
#bienvenido()
