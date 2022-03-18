import sqlite3

from bienvenido import bienvenido

def login():
    print("Inicie Sesión")
    cc = int(input("Ingrese su Nro de cedula: "))
    password=input("Ingrese su contraseña: ")
    con_bd = sqlite3.connect('database_boom.db')
    cursor_db = con_bd.cursor()    
    sql = "SELECT  Password, nombre  FROM registro WHERE Cedula=?"    
    cursor_db.execute(sql, (cc,))
    fila = cursor_db.fetchone()    
    if fila is not None:
        if password==fila[0]:
            print(f"Ingreso exitoso.") 
        else:
            print("cedula o contraseña incorrecta.")
        bienvenido()
