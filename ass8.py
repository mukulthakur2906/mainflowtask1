# Input number from user
num = int(input("Enter a number: "))

# Find the number of digits
order = len(str(num))

# Calculate the sum of digits raised to the power of 'order'
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

# Check if it is an Armstrong number
if num == sum:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
