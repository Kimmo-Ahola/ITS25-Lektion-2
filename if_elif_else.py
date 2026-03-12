# villkorsstyrd programmering


"""

Kommentarer inuti bara för att demonstrera syntaxen för if-satser
if (villkor=True/False (eller truthy/falsy)): <- kolon
    kod här <- indenterat!

# if True:
#     pass # pass = vi tar det senare

# if (True): # if kräver ett villkor
#     ... # ... samma som pass
# else: # else ska inte ha ett villkor
#     ... # pass för att koden inte ska klaga

# if True:
#     pass
# if True:
#     pass
# if True:
#     pass


# # endast en av vägarna nedan går att välja
# I detta fall är det bara en av vägarna som blir valda
# eftersom vi har en massa if/elif/else.
# if True:
#     pass
# elif False:
#     pass
# elif False:
#     pass
# elif False:
#     pass
# elif False:
#     pass
# elif False:
#     pass
# else:
#     pass


# if True:
#     # detta ger IndentationError om vi lämnar den tom
"""

# har vi elif kan vi bara ta ett av alternativen även om flera är sanna
# if 5 > 4:
#     print("Is this true?")
# elif 5 > 0:
#     print("??")
# else:
#     print("this is true!")

# True är ungefär 1
# False är ungefär 0

# print(True == 5) # exakt jämförelse. True är inte exakt 5
# 0 är Falsy och False
# if "A" == "A": # 5 truthy = typ sant
#     print("True?")
# else:
#     print("Makes no sense")

# my_number = 200

# if my_number > 4:
#     print("My number is larger than 4")
#     if my_number > 100:
#         print("Larger than 100")
#     else:
#         print("Not larger than 100")

# Felhantering
# try:
#     user_input = int(input("Ge mig en siffra: "))

#     if user_input == 0:
#         print("Noll")
#     elif user_input > 0:
#         print("Positivt")
#     elif user_input < 0:
#         print("Negativt")
# except:
#     print("Error")



from grade_checker import grade_checker

grades = [100, 85, 0, 50, 68]

for score in grades:
    grade = grade_checker(score) # gult = funktion, funktion har () efter
    print("Ditt betyg är: ", grade)