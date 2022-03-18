import sqlite3
def select_shots(ID_shots):
    con_bd = sqlite3.connect('database_boom.db')
    cursor_db = con_bd.cursor()
    sql = "SELECT Precio FROM  shots WHERE ID_shots=?"
    cursor_db.execute(sql, (ID_shots,))
    fila = cursor_db.fetchone()
    if len(fila) > 0:
        print(f"El precio del Shot es de ${fila[0]}")
        return
    print("El nombre de el shot no existe")