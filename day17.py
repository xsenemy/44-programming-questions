#44 Programming questions Code
#Very easy questions:
#17) After entering an initial amount of money and an interest rate. calculate how much money there will be after [x] years.
# Assume interest is applied once a year.
print("Whats up bro")
money = int(input("Give me money: $"))
interest = (float(input("How much yearly interest rate bro? %"))/100) + 1
years = int(input("How many years? You're safe here bro... "))

for i in range(years):
    new_money = round(money*interest, 2)
    print(f"\tYear {i+1}: ${'{:.2f}'.format(new_money)}")
    money = new_money
print(f"Ok bro, that's ${'{:.2f}'.format(new_money)} in {years}y, we're done now take your money c ya")
