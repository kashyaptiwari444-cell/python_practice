sub = int(input("howmuch subject you have: "))
marks = 0 
j = 0
for i in range(0,sub):
    m = int(input(f"Enter {i+1} mark: "))
    marks +=m
    j+=1

if marks >= 90 and marks <= 100:
    grade = "A+"
elif marks >= 80 and marks <= 89:
    grade = "A"
elif marks >= 70 and marks <= 79:
    grade = "B"
elif marks >= 60 and marks <= 69:
    grade = "C"
elif marks >= 50 and marks <= 59:
    grade = "D"
elif marks >= 40 and marks <= 49:
    grade = "E"
else:
    grade = "F (Fail)"
        

print("Total marks: ",marks)
print("Percentage is: ",marks/j)
print("Your grade is : ",grade)