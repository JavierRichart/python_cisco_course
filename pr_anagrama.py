# Esto es lo que vamos a hacer con ambas cadenas:
# - quitar los espacios
# - cambiar todas las letras a mayúsculas
# - convertirlas en listas
# - ordenar las listas
# - unir los elementos de cada lista en cadenas separadas
# y finalmente, comparar ambas cadenas.
# ¡Hagámoslo!

str_1 = input("Ingresa la primera cadena: ")
str_2 = input("Ingresa la segunda cadena: ")

strx_1 = ''.join(sorted(list(str_1.upper().replace(' ', ''))))
strx_2 = ''.join(sorted(list(str_2.upper().replace(' ', ''))))
if len(strx_1) > 0 and strx_1 == strx_2:
    print("Anagramas")
else:
    print("No son anagramas")
