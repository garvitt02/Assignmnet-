def calculate_area(length, width):
    if length == width:
        return "This is a square!"
    else:
        return length * width


length = float(input("Enter the length: "))
width = float(input("Enter the width: "))


result = calculate_area(length, width)
print(result)
