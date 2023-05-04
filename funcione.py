def suma(a,b):
    c=a+b
    return c

def resta(a,b):
    c = a-b
    return c
def algo(*args):
    for i in args:
        print(i)

def suma2(*ee):
    total = 0
    for i in ee:
        total = total + i
    return total

def algo2(**kargs):
    print(kargs)

num1 = int(input("Digita el primer número: "))
num2 = int(input("Digita el segundo número:"))
print("La suma de la suma2 es:", suma2(num1,num2))
print("La suma es: ", suma(num1,num2))
print("La resta es: ", resta(num1,num2))
algo("Roger",36,True)
algo2(nombre="ROger",edad=36,licencia= True)

