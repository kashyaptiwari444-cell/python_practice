#largest number find
much = int(input("How much you want number: "))
max = 0
min = 0
for i in range(0,much):
    num = int(input("Enter the Number: "))
    if max < num:
        max = num
print("Max Number is: ",max)
