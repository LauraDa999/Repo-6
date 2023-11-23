def calcular_valor_prestamo(C, i, n):
    valor_final = C * (1 + i)**n
    return valor_final

prestamo_inicial = 60000
tasa_interes = 0.05
num_meses = 12

valor_final_prestamo = calcular_valor_prestamo(prestamo_inicial, tasa_interes, num_meses)
print(f"El valor final del préstamo después de {num_meses} meses es: {valor_final_prestamo}")
