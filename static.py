# Modules
import os
import fileinput
import linecache

# File selector
for root, dirs, files in os.walk("./template"):
    for filename in files:
        print(filename)
filename = input("What file do you want to use? ")

# Copy the content files to the main output dir

# Replace variables from var to selected file.
i = 1
while i != 0:
    os.walk("..")
    open("var.txt", "r")
    v = linecache.getline('var.txt', i)
    if v == '': # Nothing as end of vars
        i = 0
    else:
        print("What is the variable ",v)
        a = input("[Type e for getting your editor]")
        with fileinput.FileInput("var.txt", inplace=True, backup='.bak') as file:
            for line in file:
                os.walk("./template")
                open(filename)
                print(line.replace(v, a), end='')
        i = i + 1

# Publish script
