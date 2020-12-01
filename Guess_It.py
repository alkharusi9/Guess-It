#!/usr/bin/env python3
# Written by Alsalt Alkharosi.

import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def banner():

     print(bcolors.FAIL + """     
     ______                                 ____ __ 
    / ____/__  __ ___   _____ _____        /  _// /_
   / / __ / / / // _ \ / ___// ___/______  / / / __/
  / /_/ // /_/ //  __/(__  )(__  )/_____/_/ / / /_  
  \____/ \__,_/ \___//____//____/       /___/ \__/
        # Coded By Alsalt Alkharosi - @0x_pwner
            """ + bcolors.ENDC)

def range():
    print(bcolors.OKGREEN+'''   [!] Here is a game for you to play, enter two numbers and these will be a range, then try to guess the right 
          number that was chosen randomly by the program,, ENJOY!'''+bcolors.ENDC)

    num1 = int(input(bcolors.WARNING + 'Enter your first number:' + bcolors.ENDC))
    num2 = int(input(bcolors.WARNING + 'Enter your last number:' + bcolors.ENDC))
    print(bcolors.OKGREEN + '[!] The chosen range is (' + str(num1) + '-' + str(num2) + ')' + bcolors.ENDC)

    r = random.randint(num1,num2)
    sum = r / 2
    counter = 0
    valid = False
    while not valid:
        while counter < 3:
              guess = int(input(bcolors.WARNING+'[*] Guess the right number:'+bcolors.ENDC))
              if r == guess:
                print(bcolors.OKGREEN+'[*] Well done, your guess',r,'is correct'+bcolors.ENDC)
                valid = True
                exit(1)
              elif r < guess:
                 print(bcolors.FAIL+'[-] Your guess is higher, try something smaller!'+bcolors.ENDC)
                 valid = False
                 counter += 1
              elif r > guess:
                print(bcolors.FAIL+'[-] Your guess is smaller, try something higher'+bcolors.ENDC)
                valid = False
                counter += 1
              if counter == 2:
                print(bcolors.WARNING+'[!] Hint: The number after divided by 2 is:'+bcolors.ENDC,sum)

              if counter == 3:
                print(bcolors.FAIL+'[!] 3 attempts failed, you have been locked out'+bcolors.ENDC)
                exit(1)
              else:
                pass
if __name__=='__main__':
    banner()
    range()
