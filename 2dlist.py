fruits = ("Apples", "Oranges", "Guavas", "Pineapples")
meats = ("Chicken", "Beef", "Mutton", "Turkey", "Fish")
grains = ("Rice", "Millet", "Sorghum", "Wheat")

groceries = [fruits, meats, grains]

for grocery in groceries:
    for food in grocery:
        print(food, end=" ")
    print()
