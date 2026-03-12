from pathlib import Path

# grön färg = klass = OOP
current_folder = Path.cwd() # current working directory

user_input = input("Give me a file name: ")

file_path = current_folder / user_input # inte matematisk division

if file_path.is_file() and file_path.suffix == ".txt":
    print("I found your file")
    # put your file logic here
else:
    print("Not a correct file!")