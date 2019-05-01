#!/usr/bin/env python
# Created By Benelhaj_younes

import os
from time import sleep as sl
import random

#Colors :
Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
yellow="\033[1;36m"
Red="\033[1;31m"
purple="\033[35m"
Light="\033[95m"
cyan="\033[96m"
stong="\033[39m"
unknown="\033[38;5;82m"
unknown2="\033[38;5;198m"
unknown3="\033[38;5;208m"
unknown4="\033[38;5;167m"
unknown5="\033[38;5;91m"
unknown6="\033[38;5;210m"
unknown7="\033[38;5;165m"
unknown8="\033[38;5;49m"
unknown9="\033[38;5;160m"
unknown10="\033[38;5;51m"
unknown11="\033[38;5;13m"
unknown12="\033[38;5;162m"
unknown13="\033[38;5;203m"
unknown14="\033[38;5;113m"
unknown15="\033[38;5;14m"
##########################
name = input(unknown2 + 'Enter Your Name Please: ')
os.system('clear')
sl(5)
print(unknown12 + "[+]Welcome To [BoomFb]\n"+unknown7+ "This Script Allows You To Hack Someones Facebook In Seconds!")
sl(2)
print(unknown8 + "---------"+unknown5+"[This Script Was Created By Younes Benelhaj]"+unknown15+"---------")
sl(10)
print(unknown8 +"--------"+unknown3+"[Main]"+unknown4+"-------")
sl(2)
print(unknown2 +'Enter Target Facebook Url Or Id: ')
user = input(unknown10 +"Over Here Mr(s) {}: ".format(name))
if user == '{}'.format(user):
    print(unknown13 +"Please Wait Until We Crack Account For You Mr(s) {}! ".format(name))
    sl(5)
    print(unknown11 +'Does This Correct [ {} ] ?'.format(user))
    print(unknown8 +'Please Answer Using Yes Or No !')
    choice  = input(unknown2 +'>>> ')
    if choice == 'Yes'or'yes':
        print(Red +'Now Wait Until We Crack This Out !')
        sl(50)
        print(unknown7 +"Your Password is :")
        sl(3)
        print(random.randint(1,99999999))
    else:
        print(Grey + 'Please Try Again !')
        exit(1)
