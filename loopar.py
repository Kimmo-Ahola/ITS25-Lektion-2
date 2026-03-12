# while 5: # 5 är truthy
#     # allt inuti kodblocket som är indenterat körs tills 
#     # loopen avslutas
#     print("Looping...")
# i oändliga loopar kan vi skriva ctrl + c i terminalen


while True:
    user_input = input("y to quit: ")

    if user_input == "y":
        break
	
    print("I will continue until you give me a \"y\"")


is_running = True

while is_running: # kollar alltid villkoret varje varv
    user_input = input("y to quit: ")

    if user_input == "y":
        is_running = False

counter = 0

while counter < 5:
    counter = counter + 1

print("Klar")

for i in range(20, 10, -2): # range(start, stop, step) stop != inclusive
    print(i)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers: # loopa igenom samlingar/sekvenser
    print(number)

# names = ["Kimmo", "Lars", "Göran"]

# for name in names:
#     # names[name] detta är fel
#       vi kör inte med [] i denna typen av loop
#     print(name)

for index, number in enumerate(numbers):
	if index == 5:
	    print(f"index position: {index}. Values is: {number}")


for i in range(20):
	if i % 2 == 0:
		# skriv ut alla jämna tal
		print(i)

for i in range(20):
	if i % 2: # == 0
		# i % 2 ger oss resten vid division
		# 3 % 2 = 1. 1 = truthy
		# alltså får vi alla ojämna tal
		print(i)