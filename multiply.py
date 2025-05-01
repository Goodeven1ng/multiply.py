# Mutaz Al-Shara
# Instructor Rita Ghantous
# Engr_103_401_S025
# 04-30-2025

def multiply(a, b):
    """
    Recursive function to multiply two positive integers using addition.
    
    Parameters:
    a (int): The first positive integer.
    b (int): The second positive integer.
    
    Returns:
    int: The product of a and b.
    """
    # Base case: if b is 0, return 0 (anything multiplied by 0 is 0)
    if b == 0:
        return 0
    # Recursive case: add 'a' to the result of multiply(a, b-1)
    else:
        return a + multiply(a, b - 1)

# Example usage:
print(multiply(7, 4))  # Output: 28