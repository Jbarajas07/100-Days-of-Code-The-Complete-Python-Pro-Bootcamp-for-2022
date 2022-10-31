#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")

total_bill = input("What was the total bill? $")
total_bill_data_conversion = float(total_bill)

tip_amount = input("What percentage tip would you like to give? 10, 15, 20, etc.")
tip_amount_data_conversion = int(tip_amount)

number_of_people = input("How many people will you be splitting the bill with? ")
number_of_people_data_conversion = int(number_of_people)

tip_percentage = tip_amount_data_conversion / 100
tip_in_dollars = total_bill_data_conversion * tip_percentage

total_bill_with_tip = total_bill_data_conversion + tip_in_dollars

#split_bill = round(total_bill_with_tip / number_of_people_data_conversion, 2)
split_bill = "{:.2f}".format(total_bill_with_tip / number_of_people_data_conversion) # provides the 2 decimal places, including the 0 in the hundredths place.

print(f"Each person should pay: ${split_bill}")
