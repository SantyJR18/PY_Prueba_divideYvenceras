from Funciones import *
import os

def usuarioCuenta():

    nombreTarjeta = "4000-1234-5678-9010"
    pinAccount = 9245
    nombre = input("Digite el # la tarjeta: ")
    pin = int(input("Digite su ping: "))
    if(nombreTarjeta == nombre and pin == pinAccount):
        print("Datos correctos")
        return True
    else:
        print("INTENTE DE NUEVO")
        return False
    
def deposito():
    deposit = int(input("Digite la cantidad del deposito C$: "))
    print("Su saldo viejo: C$",deposit)
    depositoCuenta(deposit)
    

def retirodeDinero():
    withdrawal = int(input("Digite la cantidad del retiro C$: "))
    retiroCuenta(withdrawal)

def menu():
            os.system("cls")
            print("1. Depositar dinero: ")
            print("2. Retirar Dinero: ")
            print("3. Mostrar cuenta: ")
            print("4. Salir.")
            op = int(input("Escriba el # de la opcion: "))
            os.system("pause") 
            return op

def main():
    if(usuarioCuenta()== True):
        op = 0
        while(op != 4):
            op = menu()
            if(op==1): 
                os.system("cls") 
                deposito()
                os.system("pause") 
            elif(op==2): 
                os.system("cls") 
                retirodeDinero()
                os.system("pause") 
            elif(op==3):
                os.system("cls") 
                mostrarCuenta()
                os.system("pause") 
            elif(op==4): 
                os.system("cls") 
                print("Gracias por usar el ATM")
            else: 
                print("Digite una opción válida")
    else:
        print("Digite bien su usuario")
    os.system("pause")

main()