#lists
#clothes = ["Shirts", "Socks", "Sweaters", "Shorts", "Pants"]
#ordered, changable, remove or add allows duplicates
#clothes.remove("Shirts")
#clothes.insert(1, "Gloves")
#clothes.sort()
#clothes.reverse()
#clothes.clear()
#print(clothes.index("Shirts"))
#print(clothes)

#sets
#fruits = {"banana", "orange", "guava", "avocado"}
#unordered, immutable, add or remove items. duplicates not allowed

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy or q to quit: ")
    if food.lower() == "q":
        break
    else:
       price = float(input(f"Enter the price of {food}: Sh "))
       foods.append(food)
       prices.append(price)


print("-----YOUR CART-----")
for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print()

print(f"Your total for foods is Sh {total}")





