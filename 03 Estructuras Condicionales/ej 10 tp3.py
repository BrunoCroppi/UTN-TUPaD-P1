#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.
hemisferio = input("¿En qué hemisferio estás? (N para norte o S para sur): ")
mes = input("¿Qué mes es? (ej. enero, febrero, etc.): ").lower()
dia = int(input("¿Qué día del mes es?: "))
meses = {"enero": 1, "febrero": 2, "marzo": 3, "abril": 4,
        "mayo": 5, "junio": 6, "julio": 7, "agosto": 8,
        "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12}
if mes not in meses:
    print ("Mes no valido")
else:
      mes_num = meses[mes]
if hemisferio == "N" or hemisferio == "n":
            if (mes_num == 12 and dia >= 21) or (1 <= mes_num <= 2) or (mes_num == 3 and dia < 21):
                print ("invierno")
            elif (mes_num == 3 and dia >= 21) or (4 <= mes_num <= 5) or (mes_num == 6 and dia < 21):
                print ("primavera")
            elif (mes_num == 6 and dia >= 21) or (7 <= mes_num <= 8) or (mes_num == 9 and dia < 23):
                print ("verano")
            else:
                print ("otoño")
elif hemisferio == "S" or hemisferio == "s":
            if (mes_num == 12 and dia >= 21) or (1 <= mes_num <= 2) or (mes_num == 3 and dia < 21):
                print("verano")
            elif (mes_num == 3 and dia >= 21) or (4 <= mes_num <= 5) or (mes_num == 6 and dia < 21):
                print("otoño") 
            elif (mes_num == 6 and dia >= 21) or (7 <= mes_num <= 8) or (mes_num == 9 and dia < 23):
                print ("Invierno")
            else:
                print ("primavera")
else:
            print("Hemisferio no válido.")


