print("Ingrese campo A: ")
num1 = int(input())
print("Ingrese campo B: ")
num2 = int(input())
print("Ingrese opción Suma [1], Resta [2]: ")
operacion = float(input())
if operacion == 1:
    if (num1>399 and num1<1000):
        if(num2>9 and num2<100):
            suma = num1 + num2
            print("La suma es "+ str(suma))
        else: print("Campo B errado")
    else: print("Campo A errado")
elif operacion == 2:
    if (num1>399 and num1<1000):
        if(num2>9 and num2<100):
            resta = num1 - num2
            print("La resta es "+ str(resta))
        else: print("Campo B errado")
    else: print("Campo A errado")        
else : print("Opción errada")