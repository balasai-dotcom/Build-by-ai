# Get a whole number from the user and convert it to an integer.
number = int(input())

# A remainder of 0 means the number is divisible by 2.
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
