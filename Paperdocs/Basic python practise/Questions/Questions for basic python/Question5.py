string = input("Enter a string: ")

if not string:
    print("The string is empty please enter a new string")
else:
    result = string[0]
    for char in string[1:]:
        if char != result[-1]:
            result = result + char

print("Result:" , result)
