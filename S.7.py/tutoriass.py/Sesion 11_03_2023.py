#Tutoría 11-03-23
#Variable: Puede almacenar datos. Es un espacio que almacena un dato especifico, una variables puede ser, como en mate, "x" y cualquier otra variable; las variables pueden ser todo tipo de letra-palabra a la que le asignemos un valor que nosotros queramos asignar
#Condicionales: if, else, elif
#Variable Constante: Nos ayudan para contener datos,  SON CONTENEDORES DE DATOS. El dato no va a cambiar. (Un número que va a ser siempre el mismo, no va a variar, no va a cambiar.)
#Var_Constante: Valor fijo que no puede cambiar en la ejecución del programa
#Asignación: 
#Complex: Números que tienen una parte reaal y una imaginaria. Al numero se le agrega una "j".
#String: Caracter que está compuesto por palabras.
#Elif: Es un "también". Para no estar poniendo "if", "else"; se escribe "elif"
#/n: Sirve para dar espacios entre valores.
#.round: Sirve para poder redondear decimales con el fin de hacer que una cantidada decimal muy grande sea mas entendible. Siempre debe ir seguido de un parentesis
#.round: Son parámetros......el parámetro al cualqueremos que llegue.
#.lower: despues del input: Hace que todas las letras, aunque vayan en mayuscula, se conviertan en minuscula.
VariableMulti1 = 5
VariableMulti2 = 6

ResultadoMulti = VariableMulti1 * VariableMulti2
print(ResultadoMulti)

"""Crear un programa que solicite 3 notas obtenidas de un curso de
programación y mediante una condición simple mostrar si aprobó
o desaprobó la materia (tener en cuenta que la nota 
para aprobar es 6)"""

not1 = float(input("Ingrese su nota 1 ->: "))
not2 = float(input("plecanIngrese su nota 2 ->: "))
not3 = float(input("Ingrese su nota 3 ->: "))
not4 = float(input("Ingrese su nota 4 ->: "))
promedio = (not1 + not2 + not3 + not4) / 4

if promedio >= 6: 
    print(f"USTED APROBO LA MATERIA CON UN PROMEDIO DE: {round(promedio, 2)}")
    print(f"USTED APROBO LA MATERIA CON UN PROMEDIO DE: {round(promedio, 2)}")
    print(f"USTED APROBO LA MATERIA CON UN PROMEDIO DE: {round(promedio, 2)}")
    print(f"USTED APROBO LA MATERIA CON UN PROMEDIO DE: {round(promedio, 2)}") 
else:
    print("NO APROBO EL CURSO, SU PROMEDIO ES DE: ", promedio).round
    
print("Fin del programa.")
