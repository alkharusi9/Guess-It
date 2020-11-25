#!/usr/bin/env python3
Written by Alsalt Alkharosi.

import random


n = random.random()
crange = input(''' 
                1) 1 - 100
                2) 100 - 200
                3) 200 - 300
                Please choose a range from above:''')

def first_range(): # 1-100
    global guess
    counter = 0
    n = random.randint(1, 100)

    valid = False
    while counter < 3:
        while not valid:
            guess = int(input('Please guess the right number:'))
            if n == guess:
                print('Good job, your guess', n, 'is correct')
                valid = True
                exit(1)
            elif n < guess:
                print('Your guess is higher than the random number, try guess something smaller!')
                counter += 1
                valid = False
            elif n > guess:
                print('Your guess is smaller than the random number, try something bigger!')
                counter += 1
                valid = False


            if counter == 3:
                print('[!] 3 attempts failed, you have been locked out!')
                exit(1)
            else:
                pass

def second_range(): # 100-200
    global guess
    counter = 0
    n = random.randint(100, 200)

    valid = False
    while counter < 3:
        while not valid:
            guess = int(input('Please guess the right number:'))
            if n == guess:
                print('Good job, your guess', n, 'is correct')
                valid = True
                exit(1)
            elif n < guess:
                print('Your guess is higher than the random number, guess something smaller!')
                counter += 1
                valid = False
            elif n > guess:
                print('Your guess is smaller than the random number, try something bigger')
                counter += 1
                valid = False


            if counter == 3:
                print('[!] 3 attempts failed, you have been locked out!')
                exit(1)
            else:
                pass

def third_range(): # 200-300
    global guess
    counter = 0
    n = random.randint(200,300)

    valid = False
    while counter < 3:
        while not valid:
            guess = int(input('Please guess the right number:'))
            if n == guess:
                print('Good job, your guess',n, 'is correct')
                valid = True
                exit(1)
            elif n < guess:
                print('Your guess is higher than the random number, guess something smaller!')
                counter += 1
                valid = False
            elif n > guess:
                print('Your guess is smaller than the random number, try something bigger')
                counter += 1
                valid = False


            if counter == 3:
                print('[!] 3 attempts failed, you have been locked out!')
                exit(1)
            else:
                pass

def main():
    if crange == '1':
        return first_range()
    elif crange == '2':
        return second_range()
    elif crange == '3':
        return third_range()
    else:
        print('Wrong range was chosen!')


if __name__=='__main__':
    main()
