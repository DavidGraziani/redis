import redis
redis_host = 'localhost'
redis_port = 6379


def principal():
    menu = """
a) Escribe la palabra panameña
b) Edita la palabra existente
c) Eliminar palabra 
d) Ver la lista de palabras
e) Buscar significado de una palabra
f) Salir
Elige: """
    eleccion = ""
    while eleccion != "f":
        eleccion = input(menu)
        if eleccion == "a":
            palabra = input("Escribe la palabra panameña: ")
            posible_significado = (palabra)
            if posible_significado:
                print(f"esta palabra '{palabra}' ya esta anotada")
            else:
                significado = input("Ingresa su significado: ")
                (palabra, significado)
                print("Palabra a sido registrada")
        
        if eleccion == "b":
            palabra = input("Ingresa la palabra que quieres editar: ")
            nuevo_significado = input("Ingresa el nuevo significado: ")
            (palabra, nuevo_significado)
            print("Palabra actualizada")
        
        if eleccion == "c":
            palabra = input("Ingresa la palabra a eliminar: ")
            (palabra)
        
        if eleccion == "d":
            palabras = ()
            print("=== Lista de palabras ===")
            for palabra in palabras:
                print(palabra[0])
        
        if eleccion == "e":
            palabra = input(
                "escribe la palabra que quieres saber su significado: ")
            significado = (palabra)
            if significado:
                print(f"El significado de '{palabra}' es:\n{significado[0]}")
            else:
                print(f"Esta palabra '{palabra}' no esta en el diccionario")
