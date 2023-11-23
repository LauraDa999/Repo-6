def calcular_cantidad_carne(N, M, K):
    peso_gallina = 6
    peso_gallo = 7
    peso_pollito = 1

    cantidad_carne = (N * peso_gallina + M * peso_gallo + K * peso_pollito)
    return cantidad_carne

cantidad_total = calcular_cantidad_carne(10, 5, 20)
print(f"La cantidad total de carne de aves es: {cantidad_total} kilos.")
