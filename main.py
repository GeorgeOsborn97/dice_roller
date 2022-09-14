import random

def get_input(prompt):
    return input(prompt)
def get_roll_count(prompt):
    return int(input(prompt))    
    
dice = get_input('dice to roll: ')  
y = get_roll_count('How many dice? ') 
print(dice)
print(y)
def rand_num(dice):
    if dice == 'd4':
        roll = (random.randrange(1, 5))
    elif dice == 'd6':
        roll = (random.randrange(1, 7))
    elif dice == 'd8':
        roll = (random.randrange(1, 9))
    elif dice == 'd10':
        roll = (random.randrange(1, 11))
    elif dice == 'd12':
        roll = (random.randrange(1, 13))
    elif dice == 'd20':
        roll = (random.randrange(1, 21))
    else:
        roll = "not a dice"  
    return roll   
x = 0
sum_dice = []
while x < y:          
    roll = rand_num(dice)
    print(roll)
    sum_dice.append(roll)
    print(sum_dice)  
    x += 1
    print(sum(sum_dice))


