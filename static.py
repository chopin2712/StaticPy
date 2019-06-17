# Modules
import os
import fileinput
import linecache
import shutil

# Will define what directory to use for the os module
file = open("dir.txt", "w")
file.write('')
file.close()
file = open("dir.txt", "r")

file.close()
file = open("dir.txt", "a")
file.write(os.getcwd())
file.write("/template/")
template = 'cmd'
file.write(template)
file.close()

file = open("dir.txt", "r")
path = file.read()
file.close()

os.chdir(path)
file = open("dir.txt", "w")
file.write(path)
file.close()

# template selector, to-do
template = 'cmd'

# File selector
i = 1
while i != 0:
    os.chdir(path)
    open("templates.txt", "r")
    l = linecache.getline('templates.txt', i)
    if l == '':
        i = 0
    else:
        print(l)
        i = i + 1

filename = input("What file do you want to use? ")
file = open("dir.txt", "a")
file.write("/")
file.write(filename)
file.close()
file = open("dir.txt", "r")
path = file.read()
print(path)



# Copy the content files to the main output dir
os.chdir(path)

os.system("ls")
# Help needed

# Replace variables from var to selected file.
i = 1
while i != 0:
    os.chdir(path)
    open("var.txt", "r")
    v = linecache.getline('var.txt', i)
    if v == '': # Nothing as end of vars
        i = 0
    else:
        print("What is the variable ",v)
        a = input("[Type e for getting your editor]")
        with fileinput.FileInput("var.txt", inplace=True, backup='.bak') as file:
            for line in file:
                os.chdir(path)
                open(filename)
                print(line.replace(v, a), end='')
        i = i + 1

# Publish script
