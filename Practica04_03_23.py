#OPERADORES LOGICOS:
#Nos sirve para trasladar, comparar o combinar dos valores (variables, etc) el que devuelve un resultado...."True" o "False" (Booleanos)
#Operadores logicos: "or" y "and" 
#Ejemplo...Operadores de Comparacion
num1 = 4
num2 = 7
respuesta1 = num1 < num2
print(respuesta1)

#OPERADORES ARITMETICOS:
num3 = 3
num4 = 9
resultado2 = num3 + num4
#En lugar de poner lo anterior, se pone lo siguiente para hacerlo mas rapido:
resultado2 = num3 + num4

#Concatenacion
resultado2 = num3 + num4
print(f"El resultado de sumar {num3} + {num4} es {resultado2}") #f-string
print("El resultado de sumar", num3, "+", num4, "es", resultado2)
print("El resultado de sumar {} + {} es {}".format(num3, num4, resultado2))
#num3 += num4
#print(num3)
print(resultado2)


#Operadores Aritmeticos: (+, -, *, **, /, //, %, )
respuesta3 = num3 ** num4
print(respuesta3)

#Módulo
num3 = 20
num4 = 8
resultado2 = num3 % num4
print(f"El resultado del modulo {num3} % {num4} = {resultado2}") #f-string
print("El resultado del modulo", num3, "%", num4, "=", resultado2)
print("El resultado del modulo {} % {} = {}".format(num3, num4, resultado2))