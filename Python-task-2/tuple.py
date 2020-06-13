student_detail = ("Priya Aggarwal", "Ridhima", "Aditya Chandel", "Deepak Kumar","Krishna","Riya Aggarwal")
print(student_detail)

print(student_detail[4])

print(student_detail[2:5])

print(student_detail[-2])

print(len(student_detail))

#looping
for x in student_detail:
    print(x)

#using tuple() method
new_detail=tuple(("Priya Aggarwal", "Ridhima", "Aditya Chandel", "Deepak Kumar","Krishna","Riya Aggarwal"))
print(new_detail)

#Adding tuple
serial_no = (1,2,3,4,5,6)
new = serial_no + student_detail
print(new)
