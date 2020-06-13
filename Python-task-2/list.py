#student details list
student_detail = ["Priya Aggarwal", "Ridhima", "Aditya Chandel", "Deepak Kumar","Krishna","Riya Aggarwal"]
print(student_detail)

print(student_detail[5])

#changing item value in a list
student_detail[2] = "Saumya Joshi"
print(student_detail)

#append
student_detail.append("Rishabh Jain")
print(student_detail)

#removing
student_detail.remove("Saumya Joshi")
print(student_detail)

#adding at a particular position
student_detail.insert(2,"Kartik")
print(student_detail)

#joing 2 list 
serial_no=[1,2,3,4,5,6]
print(serial_no + student_detail)
