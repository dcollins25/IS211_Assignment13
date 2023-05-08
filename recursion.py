def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Prompt for an integer
n = int(input("Enter an integer: "))

# Call the fibonacci function with the input from the user
result = fibonacci(n)

# Print the result
print("The", n, "th element of the Fibonacci sequence is", result)
