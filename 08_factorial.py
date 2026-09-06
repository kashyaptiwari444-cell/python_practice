# 5! = 1 × 2 × 3 × 4 × 5 = 120

num = int(input("Enter the number: "))
fact = 1
for i in range(1, num+1):
    fact *= i

print(f"factorial of {num} is : ", fact)
