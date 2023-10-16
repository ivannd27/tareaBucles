frase = input("Por favor, introduce una frase: ")
letra = input("Ahora, introduce una letra: ")

contador = 0

for caracter in frase:
    if caracter == letra:
        contador += 1

print(f"La letra '{letra}' aparece {contador} veces en la frase '{frase}'.")