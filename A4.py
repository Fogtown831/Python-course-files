for grade in range(0,100):
    grade = int(input("Please enter your grade: "))
    if grade >=90:
        print("you got an A")
    elif 80<=grade<90:
        print("you got a B")
    elif 70<=grade<80:
        print("you got a C")
    elif 60<=grade<70:
        print("you got a D")
    else:
        print("You got an F, please study next time")

