"""first_number = int(input("Ingresa el primer número: "))
second_number = int(input("Ingresa el segundo numero: "))

try:
    print(first_number / second_number)
except:
    print("Esta operación no puede ser realizada.")

print("FIN.")"""

try:
    x = int(input("Ingresa un número: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("No puedes dividir entre cero, lo siento.")
except ValueError:
    print("Debes ingresar un valor entero..")
except:
    print("Oh cielos, algo salió mal...")

print("FIN.")