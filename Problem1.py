#For this problem: This program is meant to calculate the total after tax and tip
    #One small problem!
        #For some reason, unless you put 100% for the tip, it doesn't calculate it!
        #Figure out why, and change it so that the program runs effectively
        #For full credit, add input validation (so I can not put a negative value for the price, tip, or tax rate)



meal_price = float(input("Enter the meal price: "))
tip_percentage = int(input("Enter the tip percentage: "))
tax_rate = int(input("Enter the tax rate: "))

tip = meal_price * (tip_percentage // 100)
tax = meal_price * (tax_rate // 100)

total_cost = meal_price + tip + tax

print(f"The total cost of your meal is: ${total_cost:.2f}")
