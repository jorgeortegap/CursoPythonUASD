# Definiendo las funciones


def Saludar():
    """
    Autor: Jorge Ortega
    Funcion para imprimir por pantalla "Hola"
    """
    print("Hola")


def SaludarAlguien(nombre):
    print("Hola " + nombre)


def Sumar(x, y):
    Resultado = (x + y)
    print(f"{x} + {y} = {Resultado}")


def Multiplicar(x, y):
    Resultado = (x * y)
    return Resultado


def CalcularITBIS(Monto):
    return Monto * 0.18

# Llamando las funciones
# Saludar()
# SaludarAlguien("Jorge")
# Sumar(10, 11)
# print(Multiplicar(2, 6))


print(CalcularITBIS(1000))

help(Saludar)
