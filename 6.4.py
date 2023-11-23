def calcular_vueltas(B, P, M, H):
    total_compra = P * 300 + M * 3300 + H * 350
    vueltas = B - total_compra
    return vueltas


billete = 50000
panes = 5
bolsas_leche = 2
huevos = 12

vueltas = calcular_vueltas(billete, panes, bolsas_leche, huevos)
print(f"Las vueltas (o lo que queda debiendo) son: {vueltas} pesos.")
