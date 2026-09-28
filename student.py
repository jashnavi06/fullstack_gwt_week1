student_name=input("enter your name ")
stundent_age = int(input("enter your age"))
student_roll_no  = int(input(" enter your roll no"))
print("Enter marks of subjects")
total=0
for i in range(6):
    marks=float(input("enter your marks"))
    total+=marks
    print(total)
print("total",total)
percentage=total/600*100

if percentage>100:
    print("invaild")
elif percentage>90:
    grade="A"
    print("a")
elif percentage<90 and percentage>70:
    grade="B"
    print("b")
elif percentage<70 and percentage<50:
    grade="C"
    print("c") 
else:
    grade="F"
    print("grade")

if grade=="F":
    status="fail"
else:
    status="pass"
print("### STUNDENT REPORT CARD ###")
print("stunde name", stundent_age)
print("stundent age" , stundent_age)
print("stundent roll no", student_roll_no)
print("total", total)
print("percentage", percentage)
print("grades", grade)
print("status", status)



