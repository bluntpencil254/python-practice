rows = int(input("Enter length of your shape(1 - 9): "))
columns = int(input("Enter width of your shape (1 - 9): "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
    print()