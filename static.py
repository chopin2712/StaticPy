# Need some update before (here)
import fileinput

with fileinput.FileInput("var.txt", inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace("a", "d"), end='')

import linecache

i = 1
while i != 0:
    open("var.txt", "r")
    v = linecache.getline('var.txt', i)
    if v == '': # Nothing as end of vars
        i = 0
    else:
        print("What is the variable ",v)
        a = input("[Type e for getting your editor]")
        with fileinput.FileInput("var.txt", inplace=True, backup='.bak') as file:
            for line in file:
                print(line.replace(v, a), end='')
        i = i + 1
