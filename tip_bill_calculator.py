print("Welcome to Tip bill Calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would u like to give? 10 12 15"))
people = int(input("How many people split the bill? "))
tip_as_percent = tip/100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person , 2)
print(f"Each Person should pay {final_amount} $")