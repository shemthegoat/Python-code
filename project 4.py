import random
trialNum = 0
amountoftimesrolled = 0
counter = 0
totalofi = 0
while(trialNum < 1000):   
    x=random.randint(1,6) 
    i = 1
    counter = counter + 1

    while x != 6:
        x=random.randint(1,6) 
        i = i + 1
    trialNum = trialNum + 1       
    print(i)
    totalofi = totalofi + i  
print("done")
print(counter)
print(totalofi / 1000)
