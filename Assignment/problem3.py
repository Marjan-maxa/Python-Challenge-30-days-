mark1 = float(input("Enter Bangla mark: "))
mark2 = float(input("Enter English mark: "))
mark3 = float(input("Enter Math mark: "))
mark4 = float(input("Enter Science mark: "))
mark5 = float(input("Enter ICT mark: "))
total = mark1 + mark2 + mark3 + mark4 + mark5
average = total / 5
print("Total mark :",total)
print("Average marks :",average)
if mark1<33 or mark2<33 or mark3<33 or mark4<33 or mark5<33:
    print("Status:F")
elif average>=80:
    print("Grade : A+")
    print("Status:pass")   
elif average>=70:
    print("Grade : A")
    print("Status:pass")  
elif average>=60:
    print("Grade : A-") 
    print("Status:pass")
elif average>=50:
    print("Grade : B") 
    print("Status:pass")
elif average>=40:
    print("Grade : C") 
    print("Status:pass")
else:
    print("Grade : D") 
    print("Status:pass")        