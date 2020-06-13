student_detail = {"Priya Aggarwal", "Ridhima", "Aditya Chandel", "Deepak Kumar","Krishna","Riya Aggarwal"}
print(student_detail)


#Accesing sets through loops
for x in student_detail:
    print(x)
    
#Adding multiple items using update fucntion
student_detail.update(["Ridhima","Ridhima Goyal"])
print(student_detail)

#Adding item by using add() fucntion
student_detail.add("Tapas")
print(student_detail)

#printing length
print(len(student_detail))

#Using discard() fucntion
student_detail.discard("Tapas")
print(student_detail)

#Using union() function
student_detail_new = {"Priya Aggarwal", "Tapas", "Riya Aggarwal"}
new = union(student_detail_new)
print(new)
