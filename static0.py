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
file = open(oripath, "dir.txt", "a") # Ouvrir oripath/dir.txt en a
file.write(template)
file.close()

file = open("dir.txt", "r")
os.chdir(file.read())

# Dire voici les items disponibles :
# Lister tout les dossiers
# Demander : QUel item choisissez vous
# Mettre cette variable en "filename"

# This is line 57

# Ouvrir dir.txt en append
# Ajouter /
# Ajouter la variable filename
# Fermer le fichier

# Ouvir le fichier en read
# Mettre fichier en path
# Aller à path
# Fermer le fichier

# Open file cp.txt in w
# Empty it
# Close it

# MILESTONE 75

# Open the cp.txt file in a
# add "cp -r "
# add path

# Si Filename = index or filename = page so:
#   Add /*
# Else:
#   Add post
# MILESTONE 84
# Add " "
# add oripath
# If filename == index :
#   add /output
# Elif filename == page :
# Mettre name by asking what is the name of your, filename, ??? "
#   add /output/
#   add name
# Else :
#   Mettre name by asking what is the name of your, filename, ??? "
#   add /output/
#   add name
# MILETONE 89 WARNING BLOCK 89
# Close file

# Open cp.txt in read mode
# Run > cp.txt
# os.system(run)
# Close the file cp.txt

# mettre i à 1
# Tant que i n'est pas égal à zero
#   Aller à path (to test, facultative)
#   Open var.txt in read mode
#   mettre variable v à la valeur de la ligne i dans le document var v = linecache.getline('var.txt', i)
#   If v vaut rien
#       Mettre i à 0
#   Else:
#       Write  what is the variable v
#       Mettre a à Ask type e for getting your editor
#       Remplacer v par e dans le document filename.html :
#       with fileinput.FileInput("*.html", inplace=True, backup='.bak') as file:
#           for line in file:
#               os.chdir(path)
#               open(filename)
#               print(line.replace(v, a), end='')
#       i = i + 1


# Print the differents whays to get the script
print("0 : I don't what to pulish, I just need the files")
print("1 : Using IPFS")
print("2 : Using FTP")
print("3 : Locally")

# Skip the last part for the moment
# Publish = Ask how to publish your changes
# If publish = 0 says that the result is in the output directory
#
