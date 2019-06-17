import linecache

i = 1
while i != 0:
    open("var.txt", "r")
    v = linecache.getline('var.txt', i)
    if v == '':
        i = 0
    else:
        print("What is the variable ",v)
        a = input("[Type e for getting your editor]")
        # Replace v by a in the template document
        i = i + 1
