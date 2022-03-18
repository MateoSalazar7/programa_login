import sys
import sqlite3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from login import login

def insert_registro():
    numero_mesa= int(input("Ingrese el numero de su mesa: "))
    valor = mesas_disponibles(numero_mesa)
    if valor :
        con_bd = sqlite3.connect('database_boom.db')
        cursor_db = con_bd.cursor()
        sql = "INSERT INTO registro(correo, nombre,numero_mesa, Cedula, Password) VALUES(?, ?, ?, ?, ?)"
        correo = input("Ingrese su correo: ")
        nombre = input("Ingrese su nombre: ")
        cedula=int(input("Ingrese su numero de cedula: "))
        password=input("Ingrese su contraseña: ")
        cursor_db.execute(sql, (correo,nombre,numero_mesa, cedula , password))
        con_bd.commit()
        cursor_db.close()
        proveedor_correo = 'smtp.gmail.com: 587'
        remitente = 'Losrebeldes.0203@gmail.com'
        password = 'losrebeldes123'
        servidor = smtplib.SMTP(proveedor_correo)
        servidor.starttls()
        servidor.ehlo()
        servidor.login(remitente, password)
        mensaje = "<h1>Bienvenido a Mega Boom</h1>"
        msg = MIMEMultipart()
        msg.attach(MIMEText(mensaje, 'html'))
        msg['From'] = remitente
        msg['To'] = correo
        msg['Subject'] = 'Registro Exitoso'
        servidor.sendmail(msg['From'] , msg['To'], msg.as_string())
        login()
    else:
        print ("Su mesa no esta disponoble, por favor inicie de nuevo")
        sys.exit()
def mesas_disponibles(numero_mesa):
    con_bd = sqlite3.connect('database_boom.db')
    cursor_db = con_bd.cursor()    
    sql = "SELECT *  FROM registro WHERE numero_mesa=?"    
    cursor_db.execute(sql, (numero_mesa,))
    fila = cursor_db.fetchone()    
    if fila is  None:
            return True
    else:
        return False
