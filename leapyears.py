year = int(input("Enter a year: "))

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
    if year%4!=0:
        print("Not a leap year")
    elif year%100!=0:
        print("Leap year")
    elif year%400!=0:
        print("Not a leap year")
    else:
        print("Leap year")
    #  Write the if-elif-elif-else block here.
	