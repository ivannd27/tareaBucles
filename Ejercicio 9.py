palabra = input("introduce una palabra: ")
longitud = len(palabra)

for i in range(longitud - 1, -1, -1):
    letra = palabra[i]
    print(letra)