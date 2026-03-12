# variabel sparar ett värde till en "behållare"
x = 14 # = betyder inte lika med utan tilldelning
# == är lika med

x = "Text" # typomvandling sker automatiskt i Python

heltal = 1 # heltal
annat_tal = 2.5 # flyttal
true = True # boolean
string = "1"

result = heltal + annat_tal + true

konkatenering = "Kimmo" + " " + "Ahola"

f_name = "Kimmo"
f_ename = "Ahola"

f_string = f"{f_name} {f_ename}" # formatted string
# innanför {} är interpolation


f_str = f"{2*6/4}"

filename = input("Ge mig ett filnamn: ")






name = "Kimmo"
age = 34
test = "2"

print(name, age, test)

name, test, age = age, name, test # enkelt sätt att flippa på två variabler
# tuple unpacking
print(name, age, test)