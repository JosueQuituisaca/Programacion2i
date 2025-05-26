#Reescriba el calculo de su salario con una-hora-y-media para las horas extras y cree una funcion llamada computepay (calcular salario) que toma dos parametros (horas y tarifa)
def computepay(horas, tarifa):
    if horas <= 40:
        salario = horas * tarifa
    else:
        salario = 40 * tarifa + (horas - 40) * tarifa * 1.5
    return salario
horas =int(input("Ingrese las horas trabajadas: "))
tarifa = int(input("Ingrese la tarifa por hora: "))
salario = computepay(horas, tarifa)
print("Salario: ", salario)