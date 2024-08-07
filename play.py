# def bpower(a,n):
#     pow=1
#     for i in range(n):
#         pow=pow*a
#     return pow

# def dpower(x,y):
#     if y==0:
#         return 1
#     elif y%2==0:
#         hp=dpower(x,y//2)   
#         return hp*hp
#     else:
#         hp=dpower(x,y//2)
#         return hp*hp*x

# a = int(input("Enter a: "))
# n = int(input("Enter n: "))
# print("Brute Force method a^n:", bpower(a, n))
# print("Divide and Conquer a^n:", dpower(a, n))

