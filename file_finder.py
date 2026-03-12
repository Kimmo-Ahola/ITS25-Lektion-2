try:
    with open(file="test.txt", mode="r", encoding="utf-8") as f:
        text = f.read()

    # with är en sk context manager
    # with stänger resursen åt oss automatiskt

    # print(text)
except:
    print("Error")

lines = [] # tom lista
with open("test.txt", "r", encoding="utf-8") as f:
	for line in f.readlines():
		lines.append(line) # nu kan vi spara rader enskilt
            
#print(lines)


split_text = text.split()

print(split_text)