#ciclo while
def cuenta(limite):
    i=limite
    while True:
        print(i)
        i=i -1
        if i==0:
            break
cuenta(10)

def factorial(n):
    i=2
    tmp=1
    while i<n+1:
        tmp=tmp*i
        i=i+1
    return tmp
print(factorial(4))
print(factorial(6))

#ciclo for
#iteracion en listas
for x in [1,2,3,4,5]:
    print(x)
for x in range (5):
    print(x)
for x in range (-5,2):
    print(x)
for num in ['uno','dos','tres','cuatro']:
    print(num)

#iteracion en diccionarios
elementos={'hidrogeno':1, 'helio':2, 'carbon':6}
for llave, valor in elementos.items():
    print(llave, "=", valor)
for llave in elementos.keys():
    print(llave)
for valor in elementos.values():
    print(valor)
for idx, x in enumerate(elementos):
    print('el indice es: {} y el elemento: {}'.format(idx, x))
    
def cuenta_idiom(limite):
    for i in range (limite, 0, -1):
        print(i)
    else:
        print('cuenta finalizada')
cuenta_idiom(5)

def cuenta_idiomv2(limite):
    for i in range(limite, 0, -1):
        print(i)
        if i==3:
            break
    else:
        print('cuenta finalizada')
cuenta_idiomv2(5)
