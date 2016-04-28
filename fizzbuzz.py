#FizzBuzz challenge

name = raw_input("What is your name?")
print "Hello, %s." % name

print("Hello World! Welcome to the FizzBuzz Challenge!")

varCount = 1
while(varCount < 100):
	print varCount
	varCount = varCount + 1

	if (varCount % 3 == 0) and (varCount % 5 == 0):
		print("FizzBuzz")
		varCount = varCount + 1

	elif (varCount % 3) == 0:
		print ("Fizz")
		varCount = varCount + 1

	elif (varCount % 5) == 0:
		print ("Buzz")
		varCount = varCount + 1
