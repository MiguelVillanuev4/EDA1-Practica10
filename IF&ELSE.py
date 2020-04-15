def obtenerMayorv2(param1, param2):
    if param1 < param2:
        return param2
    else:
        return param1
print("El mayor es {}".format(obtenerMayorv2(4, 20)))
print("El mayor es {}".format(obtenerMayorv2(11, 6)))

def obtenerMayor_idiom(param1, param2):
    valor=param2 if (param1 < param2) else param1
    return valor
print("El mayor es {}".format(obtenerMayor_idiom(11, 6)))
