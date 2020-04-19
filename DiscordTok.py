import random
from tkinter import filedialog
from os import path
from pathlib import Path
import pathlib


token = ""

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"

f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")


number_of_tokens = input("Number of Tokens ? \n")
number_of_tokens = int(number_of_tokens)

for c in range(number_of_tokens):

    part1 = ""
    part2 = ""
    part3 = ""

    for x in range(24):
        part1 += random.choice(chars)

    for x in range(6):
        part2 += random.choice(chars)
    for x in range(27):
        part3 += random.choice(chars)

    part1 = str(part1)
    part2 = str(part2)
    part3 = str(part3)

    part1 = part1 + "."
    part2 = part2 + "."


    token = part1 + part2 + part3

    print(token)

    text2save = str(token + "\n") # starts from `1.0`, not `0.0`
    f.write(text2save)

f.close()
    

    
    
