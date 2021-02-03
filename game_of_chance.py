import random
minval=1
maxval=6
count=1
points=[4,5,6,8,9,10]
def roll_dice():
    dice1 = random.randint(minval, maxval)
    dice2 = random.randint(minval, maxval)
    score = dice1 + dice2
    return score
score=roll_dice()
print("score:",score)
if(score==7 or score==11):
    print("you win")
elif(score==2 or score==3 or score==12 ):
    print("you lose")
elif(score in points):
    point=score
    print("roll a dice till you get",point,"points")
    score2=0
    while(point!=score2):
        print("roll a dice??(y/n)")
        game_continue=input()
        if(game_continue=="n"):
            print("you stopped the game")
            break
        else:
            score2=roll_dice()
            print("point=",score2)
            count+=1
            if(score2==7):
                print("you lose")
                break
            if(score2==point):
                print("you win in",count,"counts")



