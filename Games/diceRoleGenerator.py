'''
Dice Roll Generator
-------------------------------------------------------------
'''


import random
import os
import multiprocessing as mp

def roll_status():
    valid_responses = ['yes', 'no']
    while True:
        try:
            response = input('Do you wish to role? (Yes or No): ')
            if response.lower() not in valid_responses:
                raise ValueError('Yes or No only')

            if response.lower() == 'yes':
                return True
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                exit()

        except ValueError as err:
            print(err)

def get_dices():
    try:
        no_of_dices = int(input("Number of dice [1 to 100]: "))
        if no_of_dices < 1 or no_of_dices > 100:
            raise ValueError("number of dices shoule be between 1 - 100")
        else:
            return [None] * no_of_dices

    except ValueError as err:
        print(err)

def get_dice_choices():
    return [1, 2, 3, 4, 5, 6]

def get_value_for_dice(choices: list[int]): 
    return random.choice(choices) 

def task_wrapper(args):
    return get_value_for_dice(choices=args)

def role_dices(dices): 
    if len(dices) == 0:
        return

    dice_choices = get_dice_choices()

    print('Rolling the dice...')
    pool = mp.Pool(mp.cpu_count())
    rolled_dices = [pool.apply(task_wrapper, args = ([dice_choices] )) for dice in dices]
    pool.close()

    print('The values are:')
    print(rolled_dices)

if __name__ == '__main__':
    dices = get_dices()
    rs = roll_status()

    while rs:
        role_dices(dices)
        rs = roll_status()
