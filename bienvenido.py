from select_shots import select_shots
from select_snaks import select_snacks
def bienvenido():
    print("Bienvenido al Bar Mega Boom ")
    opcion =int(input("1.para ir al menu de bebidas \n"
                      "2. Para ir al menu de snacks \n"
                      "escriba su opcion: "))
    while opcion !=1 and opcion !=2 :
        opcion=(int(input("opcion incorecta ingrese su opcion correcta: ")))
        print(opcion)
    if opcion == 1:
        print(
        "1. Media de ron= $40.000 \n"
        "2. Botella de ron= $80.000 \n"
        "3. Litro de ron= $120.000 \n"
        "4. Media de aguardiente= $35.000 \n"
        "5. Botella de aguardiente= $75.000 \n"
        "6. Litro de aguardiente= $100.000 \n"
        "7. shot de Aguardiente = $2.000\n"
        "8. shot de Ron = $2.500\n"
        "9. shot de Tequila = $4.000\n"
        "10. shot de Vodka = $5.500 \n"
        "11. Coctel de aguardiente = $4.000\n"
        "12. Coctel de ron = $5.000\n"
        "13. Gatorade = 5.000 \n")
        id_shots= int(input("Ingrese el numero de su shot: "))
        select_shots(id_shots)


    if opcion ==2:
        print("1.Papas limon = $2000\n"
              "2.Papas pollo = $2000\n"
              "3.Gomas = $1500 \n"
              "4.Chicles = $300\n"
              "5.Choclitos = $2000\n"
              "6.Bonbonbum = $500\n"
              "7. Granizados = $3000 \n")
        id_snack=int(input("Ingrese el numero de su snack:  "))
        select_snacks(id_snack)
