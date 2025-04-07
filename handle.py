with open("new.txt", "r") as infile:
    lines = infile.readlines()
    
modified_lines = [f"{i+1}: {line.strip().upper()}\n"for i, line in enumerate(lines)]

with open("output.txt", "w") as outfile:
    outfile.writelines(modified_lines)
    
print("file successfully created")

filename = input("Enter name of file you want to read")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("\n--- file contents ---")
        print(content)
        
except FileNotFoundError:
    print(f"\n Error: the file '{filename}' does not exist")
except PermissionError:
    print(f"\n Error: You don't permission to read this file '{filename}'")
except Exception as e:
    print(f"\n An unexpected error occurred: {e}")