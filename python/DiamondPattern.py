def print_diamond(n):
    # Upper half of the diamond
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)
    
    # Lower half of the diamond
    for i in range(n - 1, 0, -1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

# Example usage
n = int(input("Enter the number of rows for the upper half: "))
print_diamond(n)
