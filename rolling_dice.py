import random
n=0
countone=0
counttwo=0
countthree=0
countfour=0
countfive=0
countsix=0
minval=1
maxval=6
while(n<100):
    dice = random.randint(minval, maxval)
    if(dice==1):
        countone+=1
    elif(dice==2):
        counttwo+=1
    elif(dice==3):
        countthree+=1
    elif(dice==4):
        countfour+=1
    elif(dice==5):
        countfive+=1
    else:
        countsix+=1
    n+=1
print("1=>",countone)
print("2=>",counttwo)
print("3=>",countthree)
print("4=>",countfour)
print("5=>",countfive)
print("6=>",countsix)