import random

def toss_coin():
    if random.random() > 0.5:
        return 'heads'
    else:
        return 'tails'
    
#Simulate 10 coin tosses
for i in range(10):
    result = toss_coin()
    print(result)