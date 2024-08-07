from itertools import combinations

def input_elements(n):
    return [int(input("Enter element: ")) for _ in range(n)]

def subset_sum(S, target_sum):
    found = False
    for i in range(len(S) + 1):
        for subset in combinations(S, i):
            if sum(subset) == target_sum:
                print(list(subset))
                found = True
    if not found:
        print(f"No subset found for the given sum {target_sum}")

# Main module
n = int(input("Enter number of elements: "))
S = input_elements(n)
print("Input set:", S)
d = int(input("Enter target sum: "))
print("The result is:")
subset_sum(S, d)
