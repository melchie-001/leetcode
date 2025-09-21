```python
def isPalindrome(x: int) -> bool:
    # Step 1: Negative numbers are not palindromes
    # Because the minus sign will appear at the end when reversed
    if x < 0:
        return False

    # Step 2: Convert the integer to a string
    # Compare it with its reverse using slicing [::-1]
    # If both are equal, it's a palindrome
    return str(x) == str(x)[::-1]
