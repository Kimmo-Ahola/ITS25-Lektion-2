# lista = list(range(20, 0, -1))
lista = list(range(20))

print("Före: ", lista)

# Sorteringsalgoritm
# Bubble sort = Den en av de sämsta algoritmerna som finns!

# keyword argument = argument som har standardvärden
def bubble_sort(lista, reversed=False): # reversed = True/False
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if not reversed:
                if lista[j] > lista[j+1]: # om värde på första pos > pos efter
                    lista[j], lista[j+1] = lista[j+1], lista[j] # då byter vi plats på dem
            else:
                if lista[j] < lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
            

# om jag inte anger något på reversed är den False som standard
bubble_sort(lista, reversed=True) # jag vill att standardbeteendet ska vara stigande
print("Efter: ", lista)

# Använd riktiga sorteringsalgoritmer inbyggda i Python
# använd sort()
# eller sorted()