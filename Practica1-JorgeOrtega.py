# 1.- Escribe en pantalla el tipo de dato que retorna la expresion 4 < 2
print(type(4 < 2))


# 2.- Almacena en una variable el nombre de una persona y al final muestra en la consola
# el mensaje: "Bienvenido [NombrePersona]"
NombrePersona = input("Por favor introduzca su nombre: ")
print("Bienvenido", NombrePersona)


# 3.- Evalue si un numero es par o impar y muestre el mensaje en consola
Numero = int(input("Por favor introduzca un numero: "))
if (Numero % 2 == 0):
    print("El numero", Numero, "es par")
else:
    print("EL numero", Numero, "es impar")


# 4.- Almacene dos numeros y evalue si el primero es mayor que el segundo. El resultado
# debe verse en la consola
Numero1 = int(input("Por favor introduzca el primer numero: "))
Numero2 = int(input("Por favor introduzca el segundo numero: "))

if (Numero1 > Numero2):
    print("El numero", Numero1, "es mayor que el numero", Numero2)
else:
    print("El numero", Numero2, "es mayor que el numero", Numero1)


# 5.- Convierta dolares a pesos
TasaDelDia = 52.25
Dolares = float(
    input("Por favor introduzca la cantidad de dolares que convertira a pesos: "))
Pesos = Dolares * TasaDelDia
print(Dolares, "es equivalente a", Pesos, "dominicanos")


# 6.- Convierta grados Celsius a Fahrenheit
Celsius = float(
    input("Por favor introduzca los grados Celsius que convertira a Fahrenheit: "))
Fahrenheit = (Celsius * 9/5) + 32
print(Celsius, "grados celsius es igual a", Fahrenheit, "grados fahrenheit")


# 7.- Almacene cuatro notas 90, 95, 77, 92 y las promedie. Al final debe decir
# su calificacion en letras A, B, C, D, E, F
Notas = 0
Materias = 0
Total = 0
while(Materias < 4):
    Notas = float(input("Por favor introduzca las cuatro notas: "))
    Total = Total + Notas
    Materias = Materias+1
    NotaFinal = Total / 4

if (NotaFinal > 100):
    print("Nota no soportada, no debe ser mayor a 100")
elif (NotaFinal >= 90):
    print("Su nota es", NotaFinal)
    print("Eres un estudiante de A")
elif (NotaFinal >= 80):
    print("Su nota es", NotaFinal)
    print("Eres un estudiante de B")
elif (NotaFinal >= 70):
    print("Su nota es", NotaFinal)
    print("Eres un estudiante de C")
elif (NotaFinal >= 60):
    print("Su nota es", NotaFinal)
    print("Eres un estudiante de D")
elif (NotaFinal >= 50):
    print("Su nota es", NotaFinal)
    print("Eres un estudiante de E")
elif (NotaFinal >= 40):
    print("Su nota es", NotaFinal)
    print("Eres un estudiante de F")
else:
    print("Nota no soportada")


# 8.- Que almacene monto, cantidad de cuotas y porcentaje de interes anual de un
# prestamo y calcule la cuota mensual. (Amortizar mediante el sistema frances)
Monto = float(
    input("Por favor introduzca el monto a solicitar prestado: "))
TiempoAnos = float(
    input("Por favor introduzca a cuantos años tomara el prestamo: "))
TasaInteresAnual = float(
    input("Por favor introduzca la tasa de interes anual: "))

TasaInteres = (TasaInteresAnual/100)

Cuota = Monto * TasaInteres * (1 + TasaInteres) ** TiempoAnos
Interes = (1 + TasaInteres) ** TiempoAnos - 1
Anual = (Cuota / Interes)
Mensual = (Anual/12)

print("")
print("Su prestamo ha sido aprobado!")
print("")
print("El valor de sus cuotas mensuales es: ", Mensual)
print("Por un periodo de", TiempoAnos*12, "meses")
print("")
