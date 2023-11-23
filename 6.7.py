def calcular_promedio(lista_numeros):
    return sum(lista_numeros) / len(lista_numeros)

def calcular_mediana(lista_numeros):
    lista_ordenada = sorted(lista_numeros)
    n = len(lista_numeros)
    if n % 2 == 0:
        medio_1 = lista_ordenada[n // 2 - 1]
        medio_2 = lista_ordenada[n // 2]
        return (medio_1 + medio_2) / 2
    else:
        return lista_ordenada[n // 2]

def calcular_promedio_multiplicativo(lista_numeros):
    producto = 1
    for numero in lista_numeros:
        producto *= numero
    return producto**(1/len(lista_numeros))

def ordenar_ascendente(lista_numeros):
    return sorted(lista_numeros)

def ordenar_descendente(lista_numeros):
    return sorted(lista_numeros, reverse=True)

def potencia_mayor_menor(lista_numeros):
    return max(lista_numeros)**min(lista_numeros)

def raiz_cubica_menor(lista_numeros):
    return min(lista_numeros)**(1/3)

numeros = []
for i in range(5):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

promedio = calcular_promedio(numeros)
mediana = calcular_mediana(numeros)
promedio_multiplicativo = calcular_promedio_multiplicativo(numeros)
ascendente = ordenar_ascendente(numeros)
descendente = ordenar_descendente(numeros)
potencia = potencia_mayor_menor(numeros)
raiz_cubica = raiz_cubica_menor(numeros)


print(f"El promedio es: {promedio}")
print(f"La mediana es: {mediana}")
print(f"El promedio multiplicativo es: {promedio_multiplicativo}")
print(f"Números ordenados de forma ascendente: {ascendente}")
print(f"Números ordenados de forma descendente: {descendente}")
print(f"La potencia del mayor elevado al menor es: {potencia}")
print(f"La raíz cúbica del menor número es: {raiz_cubica}")
