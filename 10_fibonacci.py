# Input n = 5: Output is 5 (sequence: 0, 1, 1, 2, 3)
# Enter the number of terms: 10
# Fibonacci Series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

num = int(input("Enter Number: "))
a = 0
b = 1
for i in range(num):
    print(a, end=" ")
    a, b = b, a+b 