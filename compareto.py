def compareTo(s1, s2):
    # Base case: if either string is empty, return the difference in length
    if not s1:
        return -len(s2)
    elif not s2:
        return len(s1)
    # Recursive case: compare the first characters of s1 and s2
    elif s1[0] < s2[0]:
        return -1
    elif s1[0] > s2[0]:
        return 1
    # Characters are equal, so compare the rest of the strings recursively
    else:
        return compareTo(s1[1:], s2[1:])

# Prompt for two strings
s1 = input("Enter string one: ")
s2 = input("Enter string two: ")

# Call the function to compare the two strings from the user
result = compareTo(s1, s2)

# Print the result
if result < 0:
    print(f"{s1} is less than {s2}")
elif result == 0:
    print(f"{s1} is equal to {s2}")
else:
    print(f"{s1} is greater than {s2}")
