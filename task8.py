year = int(input("Enter random year to check if it is a Leap year: "))
def leap_year():
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year")
            else: print("Not leap year")    
        else:
            print("Leap year")
    else:
        print("Not a leap year")    

leap_year()                