#!/usr/bin/env python3
Written by Alsalt Alkharosi.

import random

num1 = int(input('Enter your first number:'))
num2 = int(input('Enter your last number:'))
print('[!] The chosen range is ('+str(num1)+'-'+str(num2)+')')
def range():
    r = random.randint(num1,num2)
    counter = 0
    valid = False
    while not valid:
        while counter < 3:
            guess = int(input('[!] Guess the right number:'))
            if r == guess:
                print('[*] Well done, your guess',r,'is correct')
                valid = True
                exit(1)
            elif r < guess:
                print('[-] Your guess is higher, try something smaller!')
                valid = False
                counter +=1
            elif r > guess:
                print('[-] Your guess is smaller, try something higher')
                valid =False
                counter +=1
        if counter == 3:
            print('[!] 3 attempts failed, you have been locked out')
            exit(1)
        else:
            pass
if __name__=='__main__':
    range()
