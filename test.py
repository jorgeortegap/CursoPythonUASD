# def digitos_palindromo():
#     """
#     Esta funcion encuentra el palindromo mas grande del producto de dos numeros de 3 digitos
#     """
#     palindromo = 0
#     for i in range(100, 1000):
#         for j in range(100, 1000):
#             mult = i*j
#             if str(mult) == str(mult)[::-1] and mult > palindromo:
#                 palindromo = mult
#     print('--------------------------------------------------------------')
#     print('El numero palindromico mas grande del producto de dos numeros'
#           ' de 3 digitos es: -> ' + str(palindromo))
#     print('--------------------------------------------------------------')


# digitos_palindromo()
# input('Ingrese un numero o letra cualquiera para continuar: -> ')


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
