stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 140,
    "AMAZON": 130
}

total = 0

print("Available Stocks:")
for stock in stocks:
    print(stock, "-", stocks[stock])

while True:
    name = input("\nEnter stock name (or done): ").upper()

    if name == "DONE":
        break

    if name in stocks:
        quantity = int(input("Enter quantity: "))

        value = stocks[name] * quantity
        total += value

        print("Added:", value)

    else:
        print("Stock not available")

print("\nTotal Investment =", total)


file = open("investment.txt", "w")
file.write("Total Investment = " + str(total))
file.close()

print("Saved in investment.txt")
