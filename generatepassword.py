# PASSWORD GENERATOR

import random
from sre_parse import SPECIAL_CHARS
import string

ALL_LETTERS = string.ascii_letters
NUMBERS = '0123456789'
SPECIAL_CHARS = '+-*&%$~#!_'

ALL_SYMBOLS = ALL_LETTERS+NUMBERS+SPECIAL_CHARS

length = int(input("enter the length: "))

password = ''.join(random.sample(ALL_SYMBOLS, length))

print(f" New password generated : {password}")
