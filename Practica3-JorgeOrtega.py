# 1- Hacer una función que potencie un número x a la y


def Potenciacion(x, y):
    """
    Funcion de Python para hacer la potencia de dos numeros
    """
    return x**y


print(Potenciacion(2, 3))


# 2- Realizar una función que pida por pantalla un número del 1 al 10 y muestre
# por pantalla el número escrito en letras.

def ConvertirNumeroALetra(Numero):
    """
    Funcion que imprime por pantalla el valor en letras
    de un numero del rango 1 al 10
    """
    if Numero == 1:
        print("El numero ingresado es 'UNO'")
    elif Numero == 2:
        print("El numero ingresado es 'DOS'")
    elif Numero == 3:
        print("El numero ingresado es 'TRES'")
    elif Numero == 4:
        print("El numero ingresado es 'CUATRO'")
    elif Numero == 5:
        print("El numero ingresado es 'CINCO'")
    elif Numero == 6:
        print("El numero ingresado es 'SEIS'")
    elif Numero == 7:
        print("El numero ingresado es 'SIETE'")
    elif Numero == 8:
        print("El numero ingresado es 'OCHO'")
    elif Numero == 9:
        print("El numero ingresado es 'NUEVE'")
    elif Numero == 10:
        print("El numero ingresado es 'DIEZ'")
    else:
        print("Numero invalido, por favor ingrese un numero del 1 al 10")


ConvertirNumeroALetra(7)


# 3- Hacer una función que reciba un año como argumento y retorne
# verdadero si es bisiesto.

def AnioBisiesto(Anio):
    """
    Funcion para determinar si un año es bisiesto o no
    """
    if ((Anio % 400 == 0) or (Anio % 4 == 0) and (Anio % 100 != 0)):
        print(f"El año {Anio} es un año bisiesto")
    else:
        print(f"El año {Anio} no es un año bisiesto")


AnioBisiesto(2016)


# 4- Crear una función que evalúe dos números y retorne verdadero si ambos
# números son iguales.

def ComparacionNumeros(Numero1, Numero2):
    """
    Funcion para comparar si dos numeros son iguales o no
    """
    if (Numero1 == Numero2):
        print("Ambos numeros son iguales")
    else:
        print("Los numeros son diferentes")


ComparacionNumeros(1, 1)


# 5- Un número palindrómico se lee igual en ambos sentidos. El palíndromo más
# grande hecho del producto de dos números de 2 dígitos es 9009 = 91 × 99.
# Cree una función que encuentre el palíndromo más grande hecho del
# producto de dos números de 3 dígitos.

def isPalindrome(numero):
    if str(numero) == str(numero)[::-1]:
        return True
    else:
        return False


maxPalindrome = 1
for numero1 in range(100, 999):
    for numero2 in range(100, 999):
        producto = numero1*numero2
        if isPalindrome(producto):
            if producto > maxPalindrome:
                maxPalindrome = producto
                maxnum1 = numero1
                maxnum2 = numero2
print(maxPalindrome, maxnum1, maxnum2)


# 6- Hacer una función que reciba una cedula como argumento y diga si la
# cedula es válida o no.


def VerificadorDeCedula(Cedula):
    """
    Funcion para validar si una cedula dominicana es valida o no basada en el modulo 10

    Para mas informacion ver como calcular el digito verificador de una cedula dominicana:
    https://www.youtube.com/watch?v=__Ko7VxoCuU

    Introduzca la cedula sin guiones en formato de string (entre comillas dobles)
    """

    ListaCedula = list(Cedula)

    # Conversion de cedula en string a cedula en integer
    for i in range(0, len(ListaCedula)):
        ListaCedula[i] = int(ListaCedula[i])

    # Ejecucion de modulo 10 para conseguir el digito verificador
    # Ver video de YouTube: https://www.youtube.com/watch?v=__Ko7VxoCuU
    for x in range(len(ListaCedula)-1):
        if x % 2 != 0:
            ListaCedula[x] *= 2
            if ListaCedula[x] >= 10:
                ListaCedula[x] -= 9

    Suma = 0
    for x in range(len(ListaCedula)-1):
        Suma += ListaCedula[x]

    DigitoVerificador = str((Suma*9))
    DigitoVerificador = DigitoVerificador[-1]

    # Si el digito verificador obtenido en los calculos es igual
    # al de la cedula ingresado, la cedula es valida.
    # En caso contrario la cedula es invalida
    if (DigitoVerificador == Cedula[-1]):
        print("Esta cedula es valida")
    else:
        print("Cedula invalida, por favor intente nuevamente")


VerificadorDeCedula("00116498320")


# 7- Hacer una función que reciba como argumento una lista de elementos
# numéricos y retorno otra lista con cada elemento de la primera lista
# duplicados.

def MultiplicarLista(Lista):
    """
    Funcion para multiplicar por dos los valores de una lista

    Por favor ingrese lista en formato lista, ej: [1,2,3]
    """

    ListaMultiplicada = []
    for i in range(len(Lista)):
        ListaMultiplicada.append(Lista[i]*2)
    return ListaMultiplicada


print(MultiplicarLista([1, 2, 3]))


# 8- Hacer una función que reciba un valor iniciar y uno final, y muestre en
# pantalla las tablas de multiplicar de los números múltiplos de 6 que hay
# entre el valor inicial y el valor final.

def TablaMultiplicar(ValorInicial, ValorFinal):
    """
    Funcion que recibe un valor inicial y uno final y que muestra en pantalla 
    las tablas de multiplicar de los números múltiplos de 6 que hay entre el 
    valor inicial y el valor final.
    """
    for Tablas in range(ValorInicial, ValorFinal):
        if (Tablas % 6 == 0):
            print("=============")
            for Numeros in range(1, 11):
                print(Tablas, "X", Numeros, "=", Tablas*Numeros)


TablaMultiplicar(10, 30)
