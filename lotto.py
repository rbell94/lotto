import random


print("Today's Powerball payout is $38,500,000!")
try:
    drawings = int(int(input('Each drawing is 2 dollars, how many drawings would you like ?')))
except:
    drawings = 1


print("Pick 5 numbers ranging from 1-20.")
print("You can't choose the same number twice")

    
while True:
    number1 = input("What is your first number?")

    try: 
       number1 = int(number1)
    except ValueError:
        print("Re-pick")
        continue
    if number1 < 21:
        break
    
    print("# too high, Try Again!")   
while True:
    number2 = input("What is your second number?")
    try: 
       number2 = int(number2)
    except ValueError:
        print("Re-pick")
        continue
    if number2 == number1:
        print("I said don't %@#^&*@ choose the same #!!!")
    elif number2 < 21:
        break
    
    else:
        print("# too high, Try Again!")
while True:
    number3 = input("What is your third number?")
    try: 
       number3 = int(number3)
    except ValueError:
        print("Re-pick")
        continue
    if number3 == number2:
        print("I said don't %@#^&*@ choose the same #!!!")
    
    elif number3 == number1:
        print("I said don't %@#^&*@ choose the same #!!!")
    elif number3 < 21:
        break
    else:
        print("# too high, Try Again!")
while True:
    number4 = input("What is your fourth number?")
    try: 
       number4 = int(number4)
    except ValueError:
        print("Re-pick")
        continue
    if number4 == number3:
        print("I said don't %@#^&*@ choose the same #!!!")
    
    elif number4 == number2:
        print("I said don't %@#^&*@ choose the same #!!!")
    elif number4 == number1:
        print("I said don't %@#^&*@ choose the same #!!!")
    elif number4 < 21:
        break
    else:
        print("# too high, Try Again")
while True:
    number5 = input("What is your fifth number?")
    try: 
       number5 = int(number5)
    except ValueError:
        print("Re-pick")
        continue
    if number5 == number4:
        print("I said don't %@#^&*@ choose the same #!!!")
    
    
    elif number5 == number1:
        print("I said don't %@#^&*@ choose the same #!!!")
    elif number5 == number2:
        print("I said don't %@#^&*@ choose the same #!!!")
    elif number5 == number3:
        print("I said don't %@#^&*@ choose the same #!!!")
    elif number5 < 21:
        break
    else:
        print("# too high, Try Again!")

your_numbers = [number1, number2, number3, number4, number5]
print(f"Your numbers are: {your_numbers}")

def powerball():
    drum1 = list(range(1,20))
    drum2 = list(range(1,20))
    white_balls = []

    for _ in range(4):
        choice = random.SystemRandom().choice(drum1)
        drum1.pop(drum1.index(choice))
        white_balls.append(choice)
    white_balls = sorted(white_balls) + [random.SystemRandom().choice(drum2)]

    number_of_correct = len(list(filter(lambda n: n in (your_numbers), white_balls)))
    print(f"You got {number_of_correct} out of 5 correct!")

    amount_of_money_won = 0
    if number_of_correct < 5:
        amount_of_money_won += number_of_correct * 10
        print(f"You won ${amount_of_money_won}")
    elif number_of_correct == 0:
        print("You lost!")
    else:
        if your_numbers == white_balls:
            print("You have won the Powerball, Congradulations") 

    print(white_balls)

def random_no_repeat1(number, count):
    number_list = list(number)
    random.shuffle(number_list)
    return number_list[:count]

for _ in range(drawings):
    powerball()