# this app is smart calculator 
# you can do any numbers and you can repet it again
# GOOD LUCK

import os
os.system('cls' or 'clear')

class color:
    GREEN = '\033[92m'
    sed = '\033[96m'
    RED = '\033[91m'
    YELLOW = '\033[93m'

print(color.RED+r'                /0/000000     |0|        |0|     |1|1|            /0/000000               ')
print(color.RED+r'               /0/            |0|        |0|     |1|1|           /0/                      ')
print(color.RED+r'              /0/             |0|        |0|     |1|1|          /0/                       ')
print(color.RED+r'             /0/              |0|        |0|     |1|1|         /0/                        ')
print(color.YELLOW+r'             \0\              |0|        |0|     |1|1|         \0\                        ')
print(color.YELLOW+r'              \0\             |0|        |0|     |1|1|          \0\                       ')
print(color.YELLOW+r'               \0\            |0|        |0|     |1|1|_______    \0\                      ')
print(color.YELLOW+r'                \0\0000000     \0\000000/0/      |1|1|1|1|1|1|    \0\0000000              ')  

print('---------------------------------------------')
print('---------------------------------------------')
print('---------------------------------------------')


def calculator():

    print('you want to do  +  -  *  /')
    action = str(input('enter your action ====>'))
    numb1 = float(input('enter your number1 ====>'))
    numb2 = float(input('enter your number 2 ====>'))
    print(color.RED+'-----------------------------------------')
    if action == '/':
        print(numb1 / numb2)
    if action == '+':
        print(numb1 + numb2)
    if action == '-':
        print(numb1 - numb2)
    if action == '*':
        print(numb1 * numb2)

calculator()

print(color.RED+'-----------------------------------------')

print(color.GREEN + r' SO MANY THANKS /--\. GOOD BYE .')

