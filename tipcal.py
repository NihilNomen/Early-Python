#This is a tip calculator

#Subtotal Calculation
print("Please enter your subtotal amount: ")
mySubtotal = raw_input()
#print mySubtotal

#Tip Calculation
print("Please enter your tip percentage: ")
tipPercent = raw_input()
tipAmount = float(tipPercent) * float(mySubtotal)

print("Your tip amount is: ")
print tipAmount

#Total Calculation
total = float(mySubtotal) + float(tipAmount)
print ("Your total amount is: ")
print total
