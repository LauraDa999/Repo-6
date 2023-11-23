def calcular_contagiados_actuales(C, D):
    contagiados_futuros = C * 2**D
    return contagiados_futuros

contagiados_actuales = 50
dias_pasados = 5

contagiados_futuros = calcular_contagiados_actuales(contagiados_actuales, dias_pasados)
print(f"Después de {dias_pasados} días, el número total de contagiados será: {contagiados_futuros}")
