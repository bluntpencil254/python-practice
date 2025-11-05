menu = {"rice": 120,
        "choma ugali": 300,
        "chapati chai": 90,
        "eggs": 30,
        "chapati": 25,
        "tea": 50,
        "mandazi": 10}

cart = []
total = 0


print("------MENU------")
for key, value in menu.items():
        print(f"{key:20}: Sh {value:.2f}")
print("----------------")

while True:
        food = input("Enter food to order (q to quit): ").lower()
        if food == "q":
                break
        elif menu.get(food) is not None:
                cart.append(food)

print()
print()
print()


print("---------YOUR ORDER--------")
print(f"Your cart has: ")


for food in cart:
        total +=  menu.get(food) 
        print(food, end=" ")
print()
             
print(f"Your total is Sh {total:.2f}")
print("Thank you.")  
print()
print("-----------------")

        

