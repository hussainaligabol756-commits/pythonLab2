name=input("Enter your name: ")
roll_no=int(input("Enter your roll number: "))
English=float(input("Enter your English marks: "))
science=float(input("Enter your Science marks: "))
math=float(input("Enter your Math marks: "))
Sindhi=float(input("Enter your Sindhi marks: "))
islamiat=float(input("Enter your Islamiat marks: "))
obtained=English+science+math+Sindhi+islamiat
percent=obtained/500*100
if(English < 40 or science < 40 or math < 40 or Sindhi < 40 or islamiat < 40):result="Fail"
else:result="Pass"   
print("<<====== STUDENT'S INFORMATION ======>>")
print("The student name: ",name)
print("The student roll number: ",roll_no)
print("Marks in English: ",English)
print("Marks in Science: ",science)
print("Marks in Math: ",math)
print("Marks in Sindhi: ",Sindhi)
print("Marks in Islamiat: ",islamiat)
print("The total marks: ",obtained)
print("The percentage is : ",percent)
if (percent >=80 and percent <=100):
    print("The student grade: A+")
elif(percent >=70 and percent <80):
    print("The student grade: A")
elif(percent >=60 and percent <70):
    print("The student grade: B")
elif(percent >=50 and percent <60):
    print("The student grade: C")
elif(percent >=40 and percent <50):
    print("The student grade: D")
elif(percent < 40):
    print("Fail!")
print("The result= ",result)