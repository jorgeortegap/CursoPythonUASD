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
