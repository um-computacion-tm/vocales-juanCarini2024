def contar_vocales(mi_string):
    vocales = ("a", "e", "i", "o", "u", "à", "è", "ì", "ò", "ù")
    resultado_vocales = {}

    mi_string = mi_string.lower()  

    for letra in mi_string:
        if letra in vocales:
            if letra not in resultado_vocales:
                resultado_vocales[letra] = 0
            resultado_vocales[letra] += 1

    return resultado_vocales
    


palabra = input('Ingrese una palabra: ')
contador_vocales = contar_vocales(palabra)

total_vocales = sum(contador_vocales.values())

print("La palabra '{}' tiene {} vocales".format(palabra, total_vocales))




