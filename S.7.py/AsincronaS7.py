#TIPOS DE DATOS
#Entero (Int)
"""Realizar una multiplicación con 3 variables"""
print("MULTIPLICACION DE TRES VARIABLES: ")
varInt1 = 3
varInt2 = 2
varInt3 = 5
varInt1 = int(varInt1)
varInt2 = int(varInt2)
varInt3 = int(varInt3)
resultadoInt1 = int(varInt1 * varInt2 * varInt3)
print(resultadoInt1)
print(f"El resultado de la multiplicación de {varInt1} * {varInt2} * {varInt3} es:", (resultadoInt1))
print("""
      """)
"""Y una división entera con 2 variables distintas."""
print("DIVISION ENTERA DE DOS NUMEROS: ")
numInt1 = 12
numInt2 = 5
numInt1 = int(numInt1)
numInt2 = int(numInt2)
resultadoInt2 = int(numInt1 // numInt2)
print(resultadoInt2)
print(f"El resultado de la division entera entre {numInt1} // {numInt2} es: ", (resultadoInt2))
print("""
      """)
"""Luego sumarlos en una variable de resultados"""
print("""SUMA DE LOS RESULTADOS DE LA MULTIPLICACION 
Y DIVISION EN UNA VARIABLE DIFERENTE: """)
resultadoSumaDeVariables = int(resultadoInt1 + resultadoInt2)
print(resultadoSumaDeVariables)
print("El resultado de la suma de las variables es de: ", (resultadoSumaDeVariables))
print("""
      """)
#Flotante (Float)
'Realizar el exponencial con 2 y el modulo con 2'
print("Exponencial con 2 variables distintas: ")
variableFloat1 = 3.5
variableFloat2 = 2
totalVariables = float(variableFloat1 ** variableFloat2) 
print(totalVariables)
print("La respuesta es: ", (totalVariables))
print("""
      """)
print("Módulo de las variables: ")
resultadoModulo = float(variableFloat1 % variableFloat2)
print(resultadoModulo)
print("El resultado final del módulo de las dos variables es: ", (resultadoModulo))
print("""
      """)
'Luego restarlos en una variable de resultados'
print("Resta de los resultados de las variables anteriores: ")
restaVariables = float(totalVariables - resultadoModulo)
print(f"El resultado de la resta entre {totalVariables} y {resultadoModulo} es de: ", (restaVariables))
print("""
      """)
'Y realizar la división entre el resultado de la suma y resta'
print("División entre el resultado de la suma y resta: ")
division_suma_resta = float(resultadoSumaDeVariables / restaVariables)
print(division_suma_resta)
print(f"El resultado de la división entre {resultadoSumaDeVariables} y {restaVariables} es: ", (division_suma_resta))
print("""
      """)
#Complejo (Complex)
"Definir 4 variables complejas distintas."
print("Definición de variables complejas: ")
varUno = complex(5, + 3j)
varDos = complex(3, -2)
varTres = complex(7j)
varCuatro = complex(9, +6j)
print("Variables del tipo 'complex' ", "Primera: ", complex(varUno), "Segunda: ", complex(varDos), "Tercera: ", complex(varTres), "Cuarta: ", complex(varCuatro))
print("""
      """)
#Carácter (String)
'Defina variables según número integrantes.'
'En la variable debe almacenar el nombre de una fruta; por variable'
frut_1 = "fresa" #La fruta pertenece a: Felix Palacios
frut_2 = 'arandano' #La fruta pertenece a: Sonia Abrego
frut_3 = "uva" #La fruta pertenece a: Carlos Landaverde
frut_4 = 'ciruela' #La fruta pertenece a: Iván Membreño
frut_5 = "kiwi" #La fruta pertenece a: Marilyn Menjivar
frut_6 = 'toronja' #La fruta pertenece a: Alejandro Cañas
print(frut_1, type(frut_1))
print(frut_2, type(frut_2))
print(frut_3, type(frut_3))
print(frut_4, type(frut_4))
print(frut_5, type(frut_5))
print(frut_6, type(frut_6))
print("""
      """)
#Booleano (Bool) -Se realizará en la estructura de control IF.
"""Ingresar datos desde teclado, 
preguntar-digitar un nombre de una fruta
Y capturar ese dato en una variable."""
print("Sentencia If por cada fruta")
print("""Frutas que podrás digitar:
      Fresa
      Arandano
      Uva
      Ciruela
      Kiwi
      Toronja""")
print("""
      """)
nombreFruta = input("Ingrese el nombre de una fruta: ")
print(nombreFruta + ".")
print("""
      """)
#Estructura de control IF
"""Cada estructura definida es separada de la otra, no agrupar o tratar de hacer una sola estructura de control.
Diseñar una sentencia IF por cada fruta.
Al evaluar la expresión de cada IF si la respuesta es verdadera, 
deberá mostrar el nombre de la fruta, nombre de un compañero."""

if nombreFruta == "Fresa":
    print ("La fruta es", nombreFruta, "y pertenece al integrante del grupo: Felix Palacios." )
    print ("FIN.")
if nombreFruta == "Arandano":
    print ("La fruta es", nombreFruta, "y pertenece a la integrante del grupo: Sonia Abrego." )
    print ("FIN.")
if nombreFruta == "Uva":
    print ("La fruta es", nombreFruta, "y pertenece al integrante del grupo: Carlos Landaverde." )
    print ("FIN.")
if nombreFruta == "Ciruela":
    print ("La fruta es", nombreFruta, "y pertenece al integrante del grupo: Iván Membreño." )
    print ("FIN.")
if nombreFruta == "Kiwi":
    print ("La fruta es", nombreFruta, "y pertenece a la integrante del grupo: Marilyn Menjivar." )
    print ("FIN.")
if nombreFruta == "Toronja":
    print ("La fruta es", nombreFruta, "y pertenece al integrante del grupo: Alejandro Cañas." )
    print ("FIN.")
