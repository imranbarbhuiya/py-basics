print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? "))

tip = int(
    input(
        "What percentage tip would you like to give? (enter only number don't use percentage sign )"
    )
)

people = int(input("How many people to split the bill? "))

total_bill = round((bill * (1 + tip / 100) / people), 2)
total_bill = "{:.2f}".format(total_bill)

print(f"Each person should pay {total_bill}")
