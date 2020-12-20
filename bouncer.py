# ask for age

age = input("How old are you: ")
if age:
    age = int(age)
    if age >= 21:
        print("You are good and can drink")
    elif age >= 18:
        print("You can enter, but need wristband!")
    else:
        print("you cant come in")
else:
    print("please enter age")