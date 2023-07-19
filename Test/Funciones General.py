import re

# TIPOS DE VADIACION: cada validacion devuelve un true o un false si esta se cumple o no

# Valida que la entrada no contenga unicamente espacios vacios:
def no_spaces(entrada):
    check = entrada.replace(" ", "")
    if len(check) == 0:
        return entrada, False
    else:
        return entrada, True

# Valida que la entrada sea de tipo entero: 
def value_int_input(entrada):
    try:
        entrada = int(entrada)
        return entrada, True
    except ValueError:
        return entrada, False

# Valida que la entrada sea de tipo float:
def value_float_input(entrada):
    try:
        entrada = float(entrada)
        return entrada, True
    except ValueError:
        return entrada, False

# Valida que la entrada se encuentre dentro de un rango de numeros donde lower es el mas bajo y bigger el mas alto permitido
def range_options(entrada, lower, bigger):
    if entrada < lower or entrada > bigger:
        return entrada, False
    else:
        return entrada, True

# Valida que la entrada contenga un minimo o un maximo de caracteres donde limite_bot es el minimo y limite_top es el maximo
def input_limitado(entrada, limite_top, limite_bot):
    entrada = str(entrada)
    if len(entrada) > limite_top or len(entrada) < limite_bot:
        return entrada, False
    else:
        return entrada, True

# Valida que la entrada no contenga numeros
def no_numbers_in_str(entrada):
    entrada = str(entrada)
    if entrada.isdigit():
        return entrada, False
    else:
        return entrada, True

# Valida que la entrada no contenga caracteres especiales
def no_special_character(entrada, caracteres_permitidos=None):
    entrada = str(entrada)
    if caracteres_permitidos is None:
        patron = r'^[a-zA-Z0-9]+$'
    else:
        patron = r'^[a-zA-Z0-9{}]+$'.format(re.escape(caracteres_permitidos))
    if re.match(patron, entrada):
        return entrada, True
    else:
        return entrada, False


# TIPOS DE ENTRADAS

# Entradas int

# Verifica que la entrada no contenga solo espacios y que sea de tipo entero
def entrada_int_simple(mensaje):
    while True:
        entrada = input(mensaje)
        
        entrada, check1 = no_spaces(entrada)
        if check1 == False:
            print("\nNo se permiten entradas vacias, intente de nuevo")
            continue
        
        entrada, check2 = value_int_input(entrada)
        if check2 == False:
            print("\nTipo de entrada no valida, intente de nuevo")
            continue
        
        return entrada

# Verifica que la entrada no contenga solo espacios, que sea de tipo entero y que este dentro de un rango de numeros
def entrada_int_rango(mensaje,lower,bigger):
    while True:
        entrada = input(mensaje)
        
        entrada, check1 = no_spaces(entrada)
        if check1 == False:
            print("\nNo se permiten entradas vacias, intente de nuevo")
            continue
        
        entrada, check2 = value_int_input(entrada)
        if check2 == False:
            print("\nTipo de entrada no valida, intente de nuevo")
            continue

        entrada, check3 = range_options(entrada, lower, bigger)
        if check3 == False:
            print("\nEntrada fuera del rango de opciones, intente de nuevo")
            continue
        
        return entrada    

# Verifica que la entrada no contenga solo espacios, que sea de tipo entero y que tenga un minimo y maximo de caracteres
def entrada_int_limite(mensaje,limite_bot,limite_top):
    while True:
        entrada = input(mensaje)
        
        entrada, check1 = no_spaces(entrada)
        if check1 == False:
            print("\nNo se permiten entradas vacias, intente de nuevo")
            continue
        
        entrada, check2 = value_int_input(entrada)
        if check2 == False:
            print("\nTipo de entrada no valida, intente de nuevo")
            continue

        entrada, check3 = input_limitado(entrada, limite_top, limite_bot)
        if check3 == False:
            print("\nLa entrada debe tener un minimo de",limite_bot,"caracteres y un máximo de",limite_top,"caracteres, intente de nuevo")
            continue
        
        return entrada

# Verifica que la entrada no contenga solo espacios, que sea de tipo entero, que este dentro de un rango de numeros y que tenga un minimo y maximo de caracteres
def entrada_int_rango_limite(mensaje,lower,bigger,limite_bot,limite_top):
    while True:
        entrada = input(mensaje)
        
        entrada, check1 = no_spaces(entrada)
        if check1 == False:
            print("\nNo se permiten entradas vacias, intente de nuevo")
            continue
        
        entrada, check2 = value_int_input(entrada)
        if check2 == False:
            print("\nTipo de entrada no valida, intente de nuevo")
            continue

        entrada, check3 = range_options(entrada, lower, bigger)
        if check3 == False:
            print("\nEntrada fuera del rango de opciones, intente de nuevo")
            continue    
        
        entrada, check4 = input_limitado(entrada, limite_top, limite_bot)
        if check4 == False:
            print("\nLa entrada debe tener un minimo de",limite_bot,"caracteres y un máximo de",limite_top,"caracteres, intente de nuevo")
            continue

        return entrada    


# Entradas float

# Verifica que la entrada no contenga solo espacios y que sea de tipo float
def entrada_float_simple(mensaje):
    while True:
        entrada = input(mensaje)
        
        entrada, check1 = no_spaces(entrada)
        if check1 == False:
            print("\nNo se permiten entradas vacias, intente de nuevo")
            continue
        
        entrada, check2 = value_float_input(entrada)
        if check2 == False:
            print("\nTipo de entrada no valida, intente de nuevo")
            continue
        
        return entrada

# Verifica que la entrada no contenga solo espacios, que sea de tipo float y que este dentro de un rango de numeros
def entrada_float_rango(mensaje,lower,bigger):
    while True:
        entrada = input(mensaje)
        
        entrada, check1 = no_spaces(entrada)
        if check1 == False:
            print("\nNo se permiten entradas vacias, intente de nuevo")
            continue
        
        entrada, check2 = value_float_input(entrada)
        if check2 == False:
            print("\nTipo de entrada no valida, intente de nuevo")
            continue

        entrada, check3 = range_options(entrada, lower, bigger)
        if check3 == False:
            print("\nEntrada fuera del rango de opciones, intente de nuevo")
            continue
        
        return entrada    

# Verifica que la entrada no contenga solo espacios, que sea de tipo float y que tenga un minimo y maximo de caracteres
def entrada_float_limite(mensaje,limite_bot,limite_top):
    while True:
        entrada = input(mensaje)
        
        entrada, check1 = no_spaces(entrada)
        if check1 == False:
            print("\nNo se permiten entradas vacias, intente de nuevo")
            continue
        
        entrada, check2 = value_float_input(entrada)
        if check2 == False:
            print("\nTipo de entrada no valida, intente de nuevo")
            continue

        entrada, check3 = input_limitado(entrada, limite_top, limite_bot)
        if check3 == False:
            print("\nLa entrada debe tener un minimo de",limite_bot,"caracteres y un máximo de",limite_top,"caracteres, intente de nuevo")
            continue
        
        return entrada

# Verifica que la entrada no contenga solo espacios, que sea de tipo float, que este dentro de un rango de numeros y que tenga un minimo y maximo de caracteres
def entrada_float_rango_limite(mensaje,lower,bigger,limite_bot,limite_top):
    while True:
        entrada = input(mensaje)
        
        entrada, check1 = no_spaces(entrada)
        if check1 == False:
            print("\nNo se permiten entradas vacias, intente de nuevo")
            continue
        
        entrada, check2 = value_float_input(entrada)
        if check2 == False:
            print("\nTipo de entrada no valida, intente de nuevo")
            continue

        entrada, check3 = range_options(entrada, lower, bigger)
        if check3 == False:
            print("\nEntrada fuera del rango de opciones, intente de nuevo")
            continue    
        
        entrada, check4 = input_limitado(entrada, limite_top, limite_bot)
        if check4 == False:
            print("\nLa entrada debe tener un minimo de",limite_bot,"caracteres y un máximo de",limite_top,"caracteres, intente de nuevo")
            continue

        return entrada    


# Entradas str con validacion no_special_character

# Verifica que la entrada no contenga solo espacios y que no contenga caracteres especiales
def entrada_str_simple_nc(mensaje):
    while True:
        entrada = input(mensaje)
        
        entrada, check1 = no_spaces(entrada)
        if check1 == False:
            print("\nNo se permiten entradas vacias, intente de nuevo")
            continue
        
        entrada, check2 = no_special_character(entrada," ")
        if check2 == False:
            print("\nTipo de entrada no valida, intente de nuevo")
            continue
        
        return entrada

# Verifica que la entrada no contenga solo espacios, que no contenga caracteres especiales y que tenga un minimo y un maximo de caracters
def entrada_str_limite_nc(mensaje,limite_bot,limite_top):
    while True:
        entrada = input(mensaje)
        
        entrada, check1 = no_spaces(entrada)
        if check1 == False:
            print("\nNo se permiten entradas vacias, intente de nuevo")
            continue
        
        entrada, check2 = no_special_character(entrada," ")
        if check2 == False:
            print("\nTipo de entrada no valida, intente de nuevo")
            continue
        
        entrada, check3 = input_limitado(entrada,limite_top, limite_bot)
        if check3 == False:
            print("\nLa entrada debe tener un minimo de",limite_bot,"caracteres y un máximo de",limite_top,"caracteres, intente de nuevo")
            continue

        return entrada    

# Verifica que la entrada no contenga solo espacios, que no contenga caracteres especiales y que no contenga numeros
def entrada_str_no_numbers_nc(mensaje):
    while True:
        entrada = input(mensaje)
        
        entrada, check1 = no_spaces(entrada)
        if check1 == False:
            print("\nNo se permiten entradas vacias, intente de nuevo")
            continue
        
        entrada, check2 = no_special_character(entrada," ")
        if check2 == False:
            print("\nTipo de entrada no valida, intente de nuevo")
            continue

        entrada, check3 = no_numbers_in_str(entrada)
        if check3 == False:
            print("\nTipo de entrada no valida, intente de nuevo")
            continue

        return entrada 

# Verifica que la entrada no contenga solo espacios, que no contenga caracteres especiales, que tenga un minimo y un maximo de caracters y que no contenga numeros
def entrada_str_limite_no_numbers_nc(mensaje,limite_bot,limite_top):
    while True:
        entrada = input(mensaje)
        
        entrada, check1 = no_spaces(entrada)
        if check1 == False:
            print("\nNo se permiten entradas vacias, intente de nuevo")
            continue
        
        entrada, check2 = no_special_character(entrada," ")
        if check2 == False:
            print("\nTipo de entrada no valida, intente de nuevo")
            continue
        
        entrada, check3 = input_limitado(entrada, limite_top, limite_bot)
        if check3 == False:
            print("\nLa entrada debe tener un minimo de",limite_bot,"caracteres y un máximo de",limite_top,"caracteres, intente de nuevo")
            continue

        entrada, check4 = no_numbers_in_str(entrada)
        if check4 == False:
            print("\nTipo de entrada no valida, intente de nuevo")
            continue

        return entrada 


# Entradas str sin validacion no_special_character

# Verifica que la entrada no contenga solo espacios
def entrada_str_simple_(mensaje):
    while True:
        entrada = input(mensaje)
        
        entrada, check1 = no_spaces(entrada)
        if check1 == False:
            print("\nNo se permiten entradas vacias, intente de nuevo")
            continue
        
        return entrada

# Verifica que la entrada no contenga solo espacios y que tenga un minimo y un maximo de caracters
def entrada_str_limite(mensaje,limite_bot,limite_top):
    while True:
        entrada = input(mensaje)
        
        entrada, check1 = no_spaces(entrada)
        if check1 == False:
            print("\nNo se permiten entradas vacias, intente de nuevo")
            continue

        entrada, check2 = input_limitado(entrada,limite_top, limite_bot)
        if check2 == False:
            print("\nLa entrada debe tener un minimo de",limite_bot,"caracteres y un máximo de",limite_top,"caracteres, intente de nuevo")
            continue

        return entrada    

# Verifica que la entrada no contenga solo espacios y que no contenga numeros    
def entrada_str_no_numbers(mensaje):
    while True:
        entrada = input(mensaje)
        
        entrada, check1 = no_spaces(entrada)
        if check1 == False:
            print("\nNo se permiten entradas vacias, intente de nuevo")
            continue
        
        entrada, check2 = no_numbers_in_str(entrada)
        if check2 == False:
            print("\nTipo de entrada no valida, intente de nuevo")
            continue

        return entrada 

# Verifica que la entrada no contenga solo espacios, que tenga un minimo y un maximo de caracters y que no contenga numeros
def entrada_str_limite_no_numbers(mensaje,limite_bot,limite_top):
    while True:
        entrada = input(mensaje)
        
        entrada, check1 = no_spaces(entrada)
        if check1 == False:
            print("\nNo se permiten entradas vacias, intente de nuevo")
            continue
        entrada, check2 = input_limitado(entrada, limite_top, limite_bot)
        if check2 == False:
            print("\nLa entrada debe tener un minimo de",limite_bot,"caracteres y un máximo de",limite_top,"caracteres, intente de nuevo")
            continue

        entrada, check3 = no_numbers_in_str(entrada)
        if check3 == False:
            print("\nTipo de entrada no valida, intente de nuevo")
            continue

        return entrada 


# PRINT MENUS

# Imprime el menu principal
def print_main_menu():
    print ('\n\nCENTRO ESCOLAR "LOS MEJORES"')
    print ("\n1. Agregar alumno")
    print ("2. Agregar notas de alumno")
    print ("3. Modificar notas de alumno")
    print ("4. Eliminar alumno")
    print ("5. Mostrar lista de aprobados")
    print ("6. Mostrar lista de reprobados")
    print ("7. Mostrar toda la lista de alumnos")
    print ("8. Salir del programa")

# Imprime el menu de la opcion 3
def print_menu_2 ():
    print ("\n\nSeleccione la nota que desea modificar: ")
    print ("\n1. Tarea 1")
    print ("2. Tarea 2")
    print ("3. Actividad 1")
    print ("4. Actividad 2")
    print ("5. Examen Final")
    print ("6. Volver al menu principal")

# Imprime un menu con opciones de si o no donde question es la pregunta que desea realizar
def print_yes_no(question):
    print ("\n" + str(question))
    print ("\n1. Si")
    print ("2. No")
