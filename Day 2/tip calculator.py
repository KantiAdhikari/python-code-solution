# Project - Tip Calculator
print('Welcome to tip calculator')
bill=float(input('What was the total bill?'))
tip=int(input('How much tip would you like to give? 10, 12 or 15? '))
person=int(input('How many people to split the bill? '))
bill_with_tip = tip/100*bill+bill
bill_per_person = round(bill_with_tip/person,2)
print(f'Each person should pay: {bill_per_person}')
