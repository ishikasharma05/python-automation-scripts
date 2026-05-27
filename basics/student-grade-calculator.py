english=float(input("Enter your english marks : "))
maths=float(input("Enter your maths marks : "))
science=float(input("Enter your science marks : "))
hindi=float(input("Enter your hindi marks : "))
marathi=float(input("Enter your marathi marks : "))

total_marks=500

total=english+maths+science+hindi+marathi

print("your total marks is :" ,total)

percentage=(total/total_marks)*100

print("your precentage is : ",percentage)

if percentage < 35 :
    print("Oops , you haven't passed the exam")
    print("Better luck next time ")

elif percentage < 50 :
    print("Congratulations! , you have passed the exams but you have to work hard ")

elif percentage > 50 :
    print("Congratulations! , you have passed your exams with great percentage")

else :
    print("There's been some mistake in calculation ")
