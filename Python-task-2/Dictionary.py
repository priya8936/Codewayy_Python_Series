#Students detail
student_detail = {
    "Name" : "Priya Aggarwal",
    "College" : "DIT University",
    "year"  : "3rd"
    }
print(student_detail)

#Using key() function
print(student_detail.keys())

#using get() function
stu = student_detail.get("college")
print("\nModel of the car :-",stu)

#using value() function
print(student_detail.values())

#using item function
print("\nDetails of a student :-")
for i,j in student_detail.items():
    print(i,j)

#using len() function
print("\nLength- ",len(student_detail))

#printing all key value one by one
for x in student_detail:
  print(x)

#adding new items
student_detail["course"] = "Computer Science"
print(student_detail)
