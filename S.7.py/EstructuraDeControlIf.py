#ESTRUCTURA DE CONTROL if O Sentencia Simple
print("Sistema para calcular el promedio de u alumno")
nombre = input("Para comenzar, ¿Cuál es tu nombre? ")

funProgra = int(input(nombre + " ¿Cuál es tu calificación en Fundamentos de Programación? "))
mate = int(input(nombre + "¿Cuál es tu calificacion en matematica? "))
ingles = int(input(nombre + "¿Cual es tu calificacion en Ingles? "))

promedio = (funProgra + mate + ingles)/3
print(promedio)

if promedio >= 6: 
    print("FELICIDADES" + nombre + "APROBADO con un promedio de: ", promedio)
print("FIN")
variableString = "'Esto resalta' el texto"
variableString1 = '"Esto resalta" el texto'
print(variableString)
print(variableString1)
