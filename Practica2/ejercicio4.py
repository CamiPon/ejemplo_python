cadena = input("Ingresa la clave (debe tener menos de 10 caracteres y no␣,→contener los símbolos:@ y !):")
if len(cadena)>10: 
    print("Ingresaste más de 10 carcateres")
else:
    mensaje = "Ingresaste alguno de estos simbolos: @ p !" if "@" in cadena or "!" in cadena else "Ingreso OK"
    print(mensaje)