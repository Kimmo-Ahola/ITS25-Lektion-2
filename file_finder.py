try:
    # with är en sk context manager
    # with stänger resursen åt oss automatiskt
    
    with open(file="test.txt", mode="r", encoding="utf-8") as f:
        text = f.read()
    # print(text)
except:
    # Vi bör vara mer specifika med vår felhantering,
    # men just idag till en början är det ok med try-except som "fångar allt"
    print("Error")

lines = [] # tom lista
with open("test.txt", "r", encoding="utf-8") as f:
	for line in f.readlines():
		lines.append(line) # nu kan vi spara rader enskilt
            

# text kan vara unbound.
# om koden hamnar i except-blocket är text inte definierad
# därför är det en varning här om man kör pylance
split_text = text.split()

print(split_text)