palabra = input('Palabra a encontrar: ').upper()
grupo_letras = input('Ingresa la cadena en la que buscar: ').upper()

found = True
start = 0

for letra in palabra:
    afirmativo = grupo_letras.find(letra, start)
    if afirmativo < 0:
        found = False
        break
    start = afirmativo + 1
if found:
    print('Sí')
else:
    print('NO')