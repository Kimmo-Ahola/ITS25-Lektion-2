lista = [ ] # tom lista

# listan ska ha värden i sig

lista = [1, 2, 3, 4, 5] # i denna variabel finns det 5 värden
print(lista)

# första positionen är inte 1 utan 0
print(lista[0])

lista.append(6)
print("append = lägger till", lista)
lista.pop()
print("pop = tar bort", lista)

print(lista[-1]) # -1 = sista elementet. Kortkommando i Python

length = len(lista)
print(lista[length - 1]) # vanligt sätt att få ut sista i en lista

string = "Kimmo Ahola" # inte riktigt en lista
print("length of string: ", len(string))

print(string[-1])

# dynamiskt gör att man kan blanda datatyper
# jag rekommenderar inte att ni gör det 
# dynamisk_lista = [1, "2", 3.0, True, False, None]

# ny datatyp = None = null i andra språk
# None = ingenting, inte ens 0


# shift+tabb för att ta bort indentering
namn = input('Skriv in ditt namn: ')
lista_av_namnet = list(namn)
längden = len(lista_av_namnet)
halva = längden // 2
print(lista_av_namnet[:halva]) # slicing [start:stop:step]
print(lista_av_namnet[0]) # skriv ut första
print(lista_av_namnet[-1]) # skriv ut sista. -1 = sista