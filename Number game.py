import random
def Number_guessing():
    print("Welcome to the Number Guessing Game!!!")
    print("Start guessing the Number between 1 to 100:")
    print("You will have only 5 attempts to Guess the Number.")
    actual_number =random.randint(1,100)
    attempts=5
    while attempts>0:
        number=int(input("Enter the Number:"))
        if number==actual_number and number<=100:
            print("Congratulation!!\nYou Won the game!!!")
            exit()
        elif number<actual_number and number<=100:
            print("Oops!! the number is less than the actual number")
        elif number>actual_number and number<=100:
            print("Oops!! the number is greater than the actual number")
        else:
            print("Enter a valid input i.e.,<=100")
        attempts-=1
        print("You have only left with ",attempts,"attempts.")
    if attempts==0:
        print("You lose the game the Actual number is ",actual_number)
Number_guessing()