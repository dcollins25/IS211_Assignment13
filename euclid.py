def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Prompt for two integers
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

# Call the function using the two integers from the user
result = gcd(a, b)

# Print the result
print("The greatest common divisor of", a, "and", b, "is", result)
