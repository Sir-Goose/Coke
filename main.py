amount_due = 50

while True:
    if amount_due <= 0:
        amount_due = amount_due * -1
        print("Change owed: " + str(amount_due))
        break

    if amount_due > 0:
        print("Amount Due: " + str(amount_due))
        coin = int(input("Inset Coin: "))

    if coin == 25 or coin == 10 or coin == 5:
        amount_due = amount_due - int(coin)
