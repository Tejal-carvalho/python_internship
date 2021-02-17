import random
rollcount=0
minval=1
maxval=6
countdict={1:0,2:0,3:0,4:0,5:0,6:0}
def roll_dice():
    dice = random.randint(minval, maxval)
    return dice

while(rollcount < 100):
    dice = roll_dice()
    if dice in countdict:
        countdict[dice]+=1
    rollcount+=1

for number,count in countdict.items():
    print(number,"=>",count)
