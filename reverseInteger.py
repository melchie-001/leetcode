def reverse(x: int) -> int:
    # Define the 32-bit signed integer range
    INT_MIN, INT_MAX = -2**31, 2**31 - 1

    # Initialize the reversed number to 0
    result = 0

    # Determine the sign of the input number
    sign = -1 if x < 0 else 1

    # Work with the absolute value of x to simplify reversal
    x = abs(x)

    # Loop until all digits are processed
    while x != 0:
        # Extract the last digit
        digit = x % 10

        # Remove the last digit from x
        x //= 10

        # Check for overflow before updating result
        # If result * 10 + digit would exceed INT_MAX, return 0
        if result > (INT_MAX - digit) // 10:
            return 0

        # Append the digit to the reversed number
        result = result * 10 + digit

    # Apply the original sign and return the result
    return sign * result

# Test the function with input 5647 and print the result
print(f"{reverse(5647)}")  # Output: 7465
