# This is the first Comment

spam = 1 # and this is the second comment
         # ... and now a third!
text = "# This is not a comment because it's inside quotes"

# Using Python as a Calculator

#print(2+2)
#print(50-5*6)
#print((50-5*6)/4)
#print(8/5) # Division always returns a floating-point number

# The integer numbers (eg 2,4,-2,...) have data type int
# And the ones with fractional parts, 6.2,1.8 have data type float

# For floor division to get an integer, we use // operator
#print(17//3)
#print(17/3)
#print(17%3)
# % operator returns the remainder of the division, modulus

text = ('Put several strings within parentheses '
        'to have them joined together.')
#print(text)

# Lists
# Lists Can be written as a list of comma-separated
# values(items) between square brackets.

squares = [1,4,9,16,25]
#print(squares)

# First Steps Towards Programming,

#Fibonacci sequence

def fibonacci(n):
    fib_sequence = [0,1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence
#print(fibonacci(15))

# Dictionary

d = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
#print(d)
#print(d.values())
#print(d.keys())
#print(len(d))
print(d["one"])














