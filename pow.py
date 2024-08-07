def bpower(a, n):
    pow = 1
    for i in range(n):
        pow = pow * a
    return pow

# Divide and Conquer method
# The problem can be recursively defined by:
# dpower(x, n) = dpower(x, n / 2) * dpower(x, n / 2); // if n is even
# dpower(x, n) = x * dpower(x, n / 2) * dpower(x, n / 2); // if n is odd
def dpower(x, y):
    if y == 0:
        return 1
    elif y % 2 == 0:
        half_power = dpower(x, y // 2)
        return half_power * half_power
    else:
        half_power = dpower(x, y // 2)
        return x * half_power * half_power

# Main block
a = int(input("Enter a: "))
n = int(input("Enter n: "))
print("Brute Force method a^n:", bpower(a, n))
print("Divide and Conquer a^n:", dpower(a, n))
