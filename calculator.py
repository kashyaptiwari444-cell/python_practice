do = input("What do you want +, -, *, /, // : ")

if do in ['+', '-', '*', '/', '//']:

    time = int(input(f"How much number you want to {do} : "))
    calc = int(input("Enter 1 number: "))

    for i in range(1, time):
        num = int(input(f"Enter {i + 1} number: "))

        if do == '+':
            calc += num

        elif do == '-':
            calc -= num

        elif do == '*':
            calc *= num

        elif do == '/':
            calc /= num

        elif do == '//':
            calc //= num

    print("Calculation is =", calc)

else:
    print("Please choose correct operator: +, -, *, /, //")