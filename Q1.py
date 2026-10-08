hours=int(input("Enter the hours worked: "))
hourly_rate=int(input("Enter hourly rate: "));
if (hours <= 40):
    print("The total pay= ",hours * hourly_rate)
elif(hours > 40 ):
    total_pay=40*hourly_rate+((hours-40)*(hourly_rate*1.5))
    print("The total pay is= ",total_pay)