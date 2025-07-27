#Concession stand program

Menu = {"pizza" : 10.00,
        "pretzel" : 3.45,
        "popcorn" : 6.00,
        "lemonade" : 1.25,
        "slushies" : 3.99,
        "soda" : 2.45,
        "chips" : 1.50}

Cart = []
Total = 0

print("---------- MENU ----------")
for key, value in Menu.items():
    print(f"{key:10} : ${value:.2f}")
print("--------------------------")

while True:
    food = input("Please eneter a food you want to buy (Press q to quit): ").lower()
    if food == "q":
        break
    elif Menu.get(food) is not None:
        Cart.append(food)


print("---------- YOUR ORDER ----------")

for food in Cart:
    Total += Menu.get(food)
    print(food, end = " ")
print()

print(f"Your total is: ${Total: .2f}.")
