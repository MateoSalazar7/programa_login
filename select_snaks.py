import sqlite3

def select_snacks(ID_snacks):
    con_bd = sqlite3.connect('database_boom.db')
    cursor_db = con_bd.cursor()
    sql = "SELECT Precio FROM  snacks WHERE ID_snakcks=?"
    cursor_db.execute(sql, (ID_snacks,))
    fila = cursor_db.fetchone()
    if len(fila) > 0:
        print(f"El precio del Snack es de ${fila[0]}")
        return
    print("El nombre del snack no existe")