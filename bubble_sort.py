# lista = list(range(20, 0, -1))
lista = list(range(20))

print("Före: ", lista)

# Sorteringsalgoritm
# Bubble sort = Det är en av de sämsta algoritmerna som finns!
# Dock väldigt bra för att kunna lära sig om loopar, listor och jämförelser

# keyword argument = argument som har standardvärden
# keyword argument = måste komma efter de andra parametrarna
def bubble_sort(lista, reversed=False): # reversed ska vara en bool = True/False
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if not reversed:
                if lista[j] > lista[j+1]: # om värde på första pos > pos efter
                    lista[j], lista[j+1] = lista[j+1], lista[j] # då byter vi plats på dem
            else:
                # Här gör vi saker i omvänd ordning
                if lista[j] < lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
            

# om jag inte anger något på reversed är den False som standard
# med ett keyword argument kan jag ge ett standardbeteende till mina funktioner
# och på så sätt slippa skriva det explicit
bubble_sort(lista, reversed=True)
print("Efter: ", lista)

# Använd riktiga sorteringsalgoritmer inbyggda i Python
# använd sort()
# eller sorted()