# Take input from the user
n = int(input("Enter the number of terms: "))

# First two terms of Fibonacci sequence
a, b = 0, 1

# Check if the number of terms is valid
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci sequence up to 1 term:")
    print(a)
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
