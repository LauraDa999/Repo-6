# Repo-6 
# 3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.
```
def calcular_cantidad_carne(N, M, K):
    peso_gallina = 6
    peso_gallo = 7
    peso_pollito = 1

    cantidad_carne = (N * peso_gallina + M * peso_gallo + K * peso_pollito)
    return cantidad_carne

cantidad_total = calcular_cantidad_carne(10, 5, 20)
print(f"La cantidad total de carne de aves es: {cantidad_total} kilos.")

```
# 4. Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.
```
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

```

# 5. Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.
```
def calcular_valor_prestamo(C, i, n):
    valor_final = C * (1 + i)**n
    return valor_final

prestamo_inicial = 60000
tasa_interes = 0.05
num_meses = 12

valor_final_prestamo = calcular_valor_prestamo(prestamo_inicial, tasa_interes, num_meses)
print(f"El valor final del préstamo después de {num_meses} meses es: {valor_final_prestamo}")

```
# 6. El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.
```
```
# 7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:
-El promedio
-La mediana
-El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
-Ordenar los números de forma ascendente
-Ordenar los números de forma descendente
-La potencia del mayor número elevado al menor número
-La raíz cúbica del menor número
```
```
# 8. Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.
```
```
