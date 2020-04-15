def numeros(num):
    if num==1:
        print("tu numero es 1")
    elif num==2:
        print("tu numero es 2")
    elif num==3:
        print("tu numero es 3")
    elif num==4:
        print("tu numero es 4")
    else:
        print ("no hay opcion")
numeros(2)
numeros(5)

def numeros_idiom (num):
    if num in (1,2,3,4):
        print("tu numero es {}".format(num))
    else:
        print("{} no es una opcion".format(num))
numeros_idiom(2)
numeros_idiom(5)

def obtenerMasGrande(a,b,c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c
print("El mas grande es {}".format(obtenerMasGrande(7,13,1)))
