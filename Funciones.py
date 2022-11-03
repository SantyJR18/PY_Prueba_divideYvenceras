import Estructura
valor = 500

def depositoCuenta(deposito):
    global valor
    
    if(deposito%100==0):
        valor = valor + deposito
        print("Su saldo nuevo es: C$",valor)
    else:
        print("error en el deposito")

def retiroCuenta(retiro):
    global valor
    if retiro <= valor:
        if(retiro%100 == 0):
            valor = valor - retiro
            print("Su saldo nuevo es: C$",valor) 
    else:
        print("Digite un valor que no exceda su saldo")
        
def mostrarCuenta():
    global valor
    print("Su saldo es de: C$",valor)         