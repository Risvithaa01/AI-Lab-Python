#Student Marks,Percentage and Grade
name=input("Enter student name:")
n=int(input("Enter number of subjects"))
total=0
for i in range(1,n+1):
    mark=float(input(f"Enter mark for Subject {i}:"))
    total+=mark
percentage=total/n
if percentage>=90:
    grade="A+"
    performance="Outstanding"
elif percentage>=80:
    grade="A"
    performance="Excellant"
elif percentage>=70:
    grade="B"
    performance="Very Good"
elif percentage>=60:
    grade="C"
    performance="Good"
elif percentage>=50:
    grade="D"
    performance="Average"
else:
    grade="F"
    performance="needs improvement"
print("\n---academic performance---")
print("student name:",name)
print("total marks:",total)
print("percentage:",percentage,"%")
print("grade:",grade)
print("performance",performance)