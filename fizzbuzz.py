#FizzBuzz challenge
import time

name = raw_input("What is your name? ")

print("Hello %s! ") %(name) + ("Welcome to the FizzBuzz Challenge!")
print (" ")

print ("Fizzbuzz is a program which iterates the integers from 1 to a chosen number (In our case 100). For multiples of three print \"Fizz\" instead of the number and for the multiples of five print \"Buzz\". For numbers which are multiples of both three and five print \"FizzBuzz\"")

varCount = 1
while(varCount < 101):
	print varCount
	varCount = varCount + 1

	if (varCount % 3 == 0) and (varCount % 5 == 0):
		print("FizzBuzz")
		print(" ")
		varCount = varCount + 1
		time.sleep(0.5)

	elif (varCount % 3) == 0:
		print ("Fizz")
		print(" ")
		varCount = varCount + 1
		time.sleep(0.5)

	elif (varCount % 5) == 0:
		print ("Buzz")
		print(" ")
		varCount = varCount + 1
		time.sleep(0.5)
