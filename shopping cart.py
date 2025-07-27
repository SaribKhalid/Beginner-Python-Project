# Shopping Cart Program

Food_Items = []
Prices = []
total = 0

while True:
    Food = input("Please enter a food item (Press q to quit): ")
    if Food.lower() == "q":
        break
    else:
        price = float(input(f"Please enter the price of a {Food}: $"))
        Food_Items.append(Food)
        Prices.append(price)

print("-----YOUR SHOPPING CART-----")
for Food in Food_Items:
    print(Food)

for price in Prices:
    total += price

print(f"Your total is ${total}.")

print(Prices)