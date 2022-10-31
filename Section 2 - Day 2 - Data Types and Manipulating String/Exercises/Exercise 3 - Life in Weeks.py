# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

#    You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.

#Hint

#    There are 365 days in a year, 52 weeks in a year and 12 months in a year.
#    Try copying the example output into your code and replacing the relevant parts so that the sentence is formated the same way.


# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

days = (90 * 365) - (int(age) * 365)
weeks = (90 * 52) - (int(age) * 52)
months = (90 * 12) - (int(age) * 12)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
