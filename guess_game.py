import random
minvalue=1
maxvalue=10
count=0
number=0
play_again="y"
while(play_again=="y"):
    print("Guess the number\nI am thinking of number from 1 to 10")
    random_number=random.randint(minvalue,maxvalue)
    while(number!=random_number):
        number = int(input("Your guess:"))
        count += 1
        if (number == random_number):
            print("you have guessed in",count)
        elif(number<random_number):
            print("too low")
        else:
            print("too high")
    print("Would you want to continue? (y/n)")
    play_again = input()
    if(play_again=="n"):
        print("bye")
    else:
        count=0







