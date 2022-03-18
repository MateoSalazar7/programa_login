import sqlite3
def insert_snaks():
    con_bd = sqlite3.connect('database_boom.db')
    cursor_db = con_bd.cursor()
    sql = "INSERT INTO snacks(nombre_snacks, Precio) VALUES(?,?)"
    snack=input("Ingrese el nombre del snack: ")
    precio1= int(input("Ingrese el precio del snack: "))
    cursor_db.execute(sql, (snack, precio1))
    con_bd.commit()
    cursor_db.close()