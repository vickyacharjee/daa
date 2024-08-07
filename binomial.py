# Brute force method for calculating Binomial Coefficients using recursion
def binomialCoeff_BF(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    # Recursive call
    return binomialCoeff_BF(n - 1, k - 1) + binomialCoeff_BF(n - 1, k)

# Divide and Conquer method using dynamic programming (bottom-up approach)
def binomialCoeff_DC(n, k):
    C = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    
    # Calculate value of Binomial Coefficient in bottom-up manner
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            # Base Cases
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                # Calculate value using previously stored values
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
    
    return C[n][k]

# Main block
n = int(input("Enter n: "))
k = int(input("Enter k: "))

print("Brute Force method C(n, k):", binomialCoeff_BF(n, k))
print("Divide and Conquer method C(n, k):", binomialCoeff_DC(n, k))
