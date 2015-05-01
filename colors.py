'''This is my colors module.

'''


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

import random
def random_color():
    return random.choice([yellow, orange, red, magenta, violet, blue, cyan, green])

    


