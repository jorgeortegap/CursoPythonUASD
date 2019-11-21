# PRACTICA II PYTHON:
# 1 – Realizar un programa que solicite al usuario un número indeterminado de
# números (mientras se tecleen números que no sean cero). Al salir el programa
# debe dar en pantalla el total de números dados y la suma de ellos.

Continuar = (True)
Suma = 0
Contador = 0

while (Continuar):
    Numero = float(
        input("Por favor ingrese el numero a sumar, 0 para salir: "))
    if (Numero == 0):
        Continuar = (False)
    else:
        Suma = (Suma+Numero)
        Contador = (Contador+1)
print("Se digitaron", Contador, "numeros, para una suma total de:", Suma)


# 2- Realizar un programa que presente un menú con las siguientes opciones
#   1- Convertir grados a Celsius a Fahrenheit
#   2- Convertir dólar a pesos
#   3- Convertir metros a pies
#   4- Salir
# Cada vez que finalice una de estas acciones debe regresar al menú. El programa
# solo finalizará cuando el usuario elija la opción salir.

Continuar = (True)

while (Continuar):
    print("")
    print("Bienvenido, por favor seleccione una de las siguientes opciones")
    print("1- Convertir grados a Celsius a Fahrenheit")
    print("2- Convertir dólar a pesos")
    print("3- Convertir metros a pies")
    print("4- Salir")
    print("")
    Opcion = int(input("Introduzca opcion: "))

    if (Opcion == 1):
        print("")
        Celsius = float(
            input("Por favor introduzca los grados Celsius que convertira a Fahrenheit: "))
        Fahrenheit = (Celsius * 9/5) + 32
        print("")
        print(Celsius, "grados celsius es igual a",
              Fahrenheit, "grados fahrenheit")
    elif (Opcion == 2):
        print("")
        TasaDelDia = 52.72
        Dolares = float(
            input("Por favor introduzca la cantidad de dolares que convertira a pesos: "))
        Pesos = Dolares * TasaDelDia
        print("")
        print(Dolares, "dolares es equivalente a", Pesos, "dominicanos")
    elif (Opcion == 3):
        print("")
        Metros = float(
            input("Por favor introduzca la cantidad de metros a convertir a pies: "))
        Pies = (Metros * 3.281)
        print("")
        print(Metros, "metros es equivalente a:", Pies, "Pies")
    elif (Opcion == 4):
        print("")
        print("Hasta luego!")
        print("")
        Continuar = (False)
    else:
        print("")
        print("Opcion invalidad, por favor seleccione una opcion del 1 al 4")


# 3- Hacer un programa que genere las tablas de multiplicar de los números
# múltiplos de 5 que hay entre 1 y 1000

for Tablas in range(1, 1001):
    if (Tablas % 5 == 0):
        for Numeros in range(1, 11):
            print(Tablas, "X", Numeros, "=", Tablas*Numeros)


# 4- Realizar un programa que reciba por teclado el sueldo de un empleado y le
# aplique los cálculos de ISR (ver tabla DGII), ARS, y AFP (investigar porcentajes)

# Calculo de Descuestos
# ARS = 3.04% del salario bruto
# AFP = 2.87% del salario bruto

# Impuestos sobre la Renta (ISR)
# Escala anual	                    Tasa
# Hasta RD$416.220,00	            Exento
# RD$416.220,01 a RD$624.329,00	    15% del excedente de RD$416.220,01
# RD$624.329,01 a RD$867.123,00	    RD$31.216,00 más 20% del excedente de RD$624.329,01
# De RD$867.123,01 en adelante	    RD$79.776 más el 25% del excedente de RD$867.123,01

# Fuente: https://www.toptrabajos.com/blog/do/descuentos-de-nomina-sfs-afp-isr/

Ars = 0.0304
Afp = 0.0287
print("")
Salario = float(
    input("Por favor introduzca el salario para calcular ARS, AFP e ISR: "))
DescuentoArs = (Salario*Ars)
DescuentoAfp = (Salario*Afp)
DescuentoTotal = (DescuentoArs+DescuentoAfp)
SalarioConDescuentos = (Salario-DescuentoTotal)
SalarioAnual = (SalarioConDescuentos*12)
# Rango1 = "No Aplica"
ISR_Rango2 = 416220.01
ISR_Rango3 = 624329.01
ISR_Rango4 = 867123.01
ISR_ExcendenteAnualRango2 = ((SalarioAnual - ISR_Rango2)*0.15)
ISR_ExcendenteAnualRango3 = (((SalarioAnual - ISR_Rango3)*0.20)+31216)
ISR_ExcendenteAnualRango4 = (((SalarioAnual - ISR_Rango4)*0.25)+79776)
ISR_ExcendenteMensual2 = (ISR_ExcendenteAnualRango2/12)
ISR_ExcendenteMensual3 = (ISR_ExcendenteAnualRango3/12)
ISR_ExcendenteMensual4 = (ISR_ExcendenteAnualRango4/12)
DescuentoTotalRango2 = (DescuentoTotal+ISR_ExcendenteMensual2)
DescuentoTotalRango3 = (DescuentoTotal+ISR_ExcendenteMensual3)
DescuentoTotalRango4 = (DescuentoTotal+ISR_ExcendenteMensual4)
SalarioConDescuentosRango2 = (Salario - DescuentoTotalRango2)
SalarioConDescuentosRango3 = (Salario - DescuentoTotalRango3)
SalarioConDescuentosRango4 = (Salario - DescuentoTotalRango4)

# print(Salario)
# print(DescuentoArs)
# print(DescuentoAfp)
# print(DescuentoTotal)
# print(SalarioConDescuentos)
# print(SalarioAnual)

if (SalarioAnual <= 416220.00):
    print("")
    print("Su salario bruto es:", Salario)
    print("Descuento de ARS:", DescuentoArs)
    print("Descuento de AFP:", DescuentoAfp)
    print("Descuento de ISR: Su sueldo esta exento de ISR")
    print("Total de descuentos:", DescuentoTotal)
    print("Su sueldo neto despues de descuentos es:", SalarioConDescuentos)
    print("")
elif (SalarioAnual >= 416220.01 and SalarioAnual <= 624329.00):
    print("")
    print("Su salario bruto es:", Salario)
    print("Descuento de ARS:", DescuentoArs)
    print("Descuento de AFP:", DescuentoAfp)
    print("Descuento de ISR:", ISR_ExcendenteMensual2)
    print("Total de descuentos:", DescuentoTotalRango2)
    print("Su sueldo neto despues de descuentos es:", SalarioConDescuentosRango2)
    print("")
elif (SalarioAnual >= 624329.01 and SalarioAnual <= 867123.00):
    print("")
    print("Su salario bruto es:", Salario)
    print("Descuento de ARS:", DescuentoArs)
    print("Descuento de AFP:", DescuentoAfp)
    print("Descuento de ISR:", ISR_ExcendenteMensual3)
    print("Total de descuentos:", DescuentoTotalRango3)
    print("Su sueldo neto despues de descuentos es:", SalarioConDescuentosRango3)
    print("")
elif (SalarioAnual >= 867123.01):
    print("")
    print("Su salario bruto es:", Salario)
    print("Descuento de ARS:", DescuentoArs)
    print("Descuento de AFP:", DescuentoAfp)
    print("Descuento de ISR:", ISR_ExcendenteMensual4)
    print("Total de descuentos:", DescuentoTotalRango4)
    print("Su sueldo neto despues de descuentos es:", SalarioConDescuentosRango4)
    print("")


# 5-Cree una aplicación de cajero automático para el banco ABC. El cajero tendrá un
# límite de billetes descrito a continuación: 9 de 1000, 19 de 500, 99 de 100
# El cajero debe solicitar Banco y monto a retirar. Si el banco es ABC el limite de
# retiro son 10,000 y 2000 pesos por transacción en caso contrario.
# El cajero debe informar si el monto solicitado no puede ser dispensado o si
# excede el límite de transacción. Y debe hacer la distribución de los billetes de
# acuerdo al monto. Por ejemplo, si el usuario solicita 3,900 y hay disponibilidad en
# todos los billetes, el cajero debe dispensar 3 billetes de mil, 1 de quinientos y 4 de
# cien.
