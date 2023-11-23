# Repo 6 

# 1. Respecto a la Figura1 :
-Una función matemática para calcular el volumen y el área superficial.
-Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.
-Revise como utilizar el valor de pi usando import math y math.pi
```
import math
def calcular_volumenYareaS(r1, r2, h):
    volumen_esfera = (4 / 3) * math.pi * r1 ** 3
    area_superficial_esfera = 4 * math.pi * r1 ** 2
    volumen_cono = (1 / 3) * math.pi * r2 ** 2 * h
    area_superficial_cono = math.pi * r2 * (r2 + math.sqrt(r2 ** 2 + h ** 2))
    return {
      "volumen_esfera": volumen_esfera,
      "area_superficial_esfera": area_superficial_esfera,
      "volumen_cono": volumen_cono,
      "area_superficial_cono": area_superficial_cono,
  }
def datos():
  r1 = float(input("Introduce el radio de la esfera: "))
  r2 = float(input("Introduce el radio de la base del cono: "))
  h = float(input("Introduce la altura del cono: "))
  return r1, r2, h
r1, r2, h = datos()
resultado = calcular_volumenYareaS(r1, r2, h)
print(resultado)
```


# 2. Respecto a la figura 2:
-Una función matemática para calcular el área y el perimetro.
-Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.
-Revise como utilizar el valor de pi usando import math y math.pi
```
import math
def calcular_area_y_perimetro_circulo(r):
  area_circulo = math.pi * r ** 2
  perimetro_circulo = 2 * math.pi * r
  return {
      "area_circulo": area_circulo,
      "perimetro_circulo": perimetro_circulo,
  }
def calcular_area_y_perimetro_rectangulo(a, b):
  area_rectangulo = a * b
  perimetro_rectangulo = 2 * (a + b)
  return {
      "area_rectangulo": area_rectangulo,
      "perimetro_rectangulo": perimetro_rectangulo,
  }
def calcular_area_y_perimetro_cuadrado(a):
  return calcular_area_y_perimetro_rectangulo(a, a)
r = float(input("Introduce el radio del círculo: "))
resultado_circulo = calcular_area_y_perimetro_circulo(r)
print(resultado_circulo)
a = float(input("Introduce el ancho del rectángulo: "))
b = float(input("Introduce el alto del rectángulo: "))
resultado_rectangulo = calcular_area_y_perimetro_rectangulo(a, b)
print(resultado_rectangulo)
```

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
def calcular_contagiados_actuales(C, D):
    contagiados_futuros = C * 2**D
    return contagiados_futuros

contagiados_actuales = 50
dias_pasados = 5

contagiados_futuros = calcular_contagiados_actuales(contagiados_actuales, dias_pasados)
print(f"Después de {dias_pasados} días, el número total de contagiados será: {contagiados_futuros}")

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

```
# 9. Consultar qué es y cómo funciona pip en python:
Pip en python es un sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python y descargarlos a nuestra computadora con la finalidad de integrarlos a nuestros desarrollos realizado en python

# 10. Hacer un listado de módulos populares para python que se puedan instalar com pip y consultar cómo instalarlos.

-NumPy es una biblioteca para cálculo numérico. Proporciona una estructura de datos de matriz multidimensional y funciones para realizar operaciones matemáticas y estadísticas en matrices. pip install numpy
-SciPy es una biblioteca para ciencia e ingeniería. Proporciona una amplia gama de funciones para el análisis de datos, la simulación numérica y el aprendizaje automático. pip install scipy
-Pandas es una biblioteca para análisis de datos. Proporciona estructuras de datos y herramientas para manipular y analizar datos tabulados. pip install pandas
-Matplotlib es una biblioteca para visualización de datos. Proporciona funciones para crear gráficos y diagramas. pip install matplotlib

