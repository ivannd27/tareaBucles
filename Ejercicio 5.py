inversion = int(input("Cuanto vas a invertir? :"))
interes = int(input("¿Cual es el interes?"))
años = int(input("¿Durante cuantos años?"))

interes_decimal = interes / 100

for años in range(1, años + 1):
    print(inversion*interes_decimal)