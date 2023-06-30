def saludar():
    print("HELLO WORLD")

saludar()
    
def f(x):
    return 2**x
y = f(3)
print(y) # 6
    
    
def potencia(base, exponente):
    return base**exponente

resultado = potencia(2,3)
print(resultado) 
print(potencia(2,8))    



def potencia(base, exponente):
    print (base**exponente)

potencia(2,16)    

print("")

def suma(a,b):
    print(a+b)

def resta(a,b):
    print(a-b)

def multiplicacion(a,b):
    print(a*b)

def division(a,b):
    print(a/b)


n1=int(input("teclea el primer valor : "))
n2=int(input("teclea el segundo valor : "))
print("Menu")
print("1.- suma")
print("2.- resta")
print("3.- multiplicacion")
print("4.- division")
opcion= int (input("cual es la opcion elige : "))



if opcion==1:
    suma(n1,n2)
elif opcion==2:
    resta(n1,n2)
elif opcion==3:
    multiplicacion(n1,n2)
elif opcion==4:
    division(n1,n2)