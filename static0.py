# Modules imports
import os
import fileinput
import linecache
import shutil

file = open("dir.txt", "w")
file.write("")
file.close()

file = open("dir.txt", "a")
file.write(os.getcwd())
oripath = os.getcwd()
file.write("/template")
file.close()
file = open("dir.txt", "r")
path = file.read()
file.close()

os.chdir(path)
print("This is the avaiable templates")
os.system("ls -d */")
template = input("Which template do you choose? ")

# The following line is experimental

file = open("dirpath.txt", "w")
file.write("")
file.close()
file = open("dirpath.txt", "a")
file.write(oripath)
file.write("/dir.txt")
file.close()
file = open("dirpath.txt", "r")
dirpath = file.read()
file.close()
file = open(dirpath, "a") # Ouvrir oripath/dir.txt en a
file.write("/")
file.write(template)
file.close()

file = open(dirpath, "r")
os.chdir(file.read())

print("This is the avaiable items:")
os.system("ls -d */")
filename = input("What item do you want: ")

file = open("dir.txt", "a")
file.write("/")
file.write(filename)
file.close()

file = open("dir.txt", "r")
path = file.read()
os.chdir(path)
file.close()

file = open("cp.txt", "w")
file.write("")
file.close()

file = open("cp.txt", "a")
file.write("cp -r ")
file.write(path)

if filename == index or filename == page:
    file.write("/*")
else:
    file.write(post)

file.write(" ")
file.write(oripath)

if filename == index:
    file.write("/output")
elif filename == page:
    name = input("what is your ", filename, "??? ")
    file.write("/output/")
    file.write(name)
else:
    name = input("What is your ", filename, "??? ")
    file.write("/output/")
    file.write(name)
    file.close()

file = open("cp.txt", "r")
run = file.read()
os.system(run)
file.close()

i = 1
while i != 0:
    os.chdir(path) #   Aller à path (to test, facultative)
    file = open("var.txt", "r")
    v = linecache.getline('var.txt', i)
    if v == '':
        i = 0
    else:
        print("What is the value of variable", v)
        a = input("[Type e for getting your editor]")
        if a == "e":
            print("not made yet")
        else:
            with fileinput.FileInput("var.txt", inplace=True, backup='.bak') as file:
                for line in file:
                    os.chdir(path)
                    open(filename)
                    print(line.replace(v, a), end='')
            i = i + 1


# Print the differents whays to get the script
print("0 : I don't what to pulish, I just need the files")
print("1 : Using IPFS")
print("2 : Using FTP")
print("3 : Locally")

# Skip the last part for the moment
publish = input("How to you what to upload your changes")
if publish == '0':
    print("DONE: Your result is in the output directory")
