'''This is my colors module.

'''

import random as r

base01 = '\033[1;32m'
base00 = '\033[1;33m'
base0 = '\033[1;34m'
base1 = '\033[1;36m'
base2 = '\033[0;37m'
base3 = '\033[1;37m'
yellow = '\033[0;33m'
orange = '\033[1;31m'
red = '\033[0;31m'
magenta = '\033[0;35m'
violet = '\033[1;35m'
blue = '\033[0;34m'
cyan = '\033[0;36m'
green = '\033[0;32m'
reset = '\033[0m'
clear = '\033[H\033[2J'

colors = [clear,base00, base01, base0, base1, base2, base3, yellow, orange, 
red, magenta, violet, blue, cyan, green, reset]
def random_color():
    color = r.choice(colors)
    return color
if __name__ == '__main__':
    print(clear)
    for color in colors:
        print(color + 'Go Blockmc' + reset)

