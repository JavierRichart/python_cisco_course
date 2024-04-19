print('peDrO'.capitalize())
print('(' + 'mono'.center(20) + ')')
print('(' + 'mono'.center(16) + ')')
print('(' + 'mono'.center(12) + ')')
print('(' + ' mono '.center(20, '*') + ')')

if "mono".endswith('no'):
    print('mono termina en no')
else:
    print('no')

print('mono'.find('no'))
print('mono'.find('on'))

print('kappa'.find('a', 2))
print('panorama'.find('a', 3))

print('notino33'.isalnum())
print('30'.isalnum())
print('notino'.isalnum())
print(''.isalnum())
print('*'.isalnum())

print('notino'.isalpha())

print('2018'.isdigit())

cadena1 = ['marte', 'venus', 'jupiter', 'tierra', 'sol', 'urano', 'neptuno', 'mercurio']
cadena2 = sorted(cadena1)
print(cadena2)
cadena1.sort()
print(cadena1)

year = 2024
year_str = str(year)