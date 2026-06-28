def saludar(nombre_completo):

    if nombre_completo.strip() == "":
        return "Error: El nombre no puede estar vacío."

    return f"Hola {nombre_completo}"


print(saludar("GitHub"))
print(saludar(""))