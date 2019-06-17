secure = 0
file = open("secure", "r")
secure = file.read()
file.close()

while secure == 0:
    # The sitename variable is always in first line
    sitename = input("What is your sitename? ")
    file = open("var", "a")
    file.write(sitename)
    file.write("\n")
    file.close()

    template = input("What is your template name? ")
    file = open("var", "a")
    file.write(template)
    file.write("\n")
    file.close()

    w = 1
    while w == 1:
        new_home = input("Do you want to create a new home page? [Y, n] ")

        if new_home == 'y' or new_home == 'Y':
            print("Working 1")
            w = 0
        elif new_home == 'n' or new_home == 'N':
            print("working 2")
            w = 0
        else:
            print("Not valid answer.")
            w = 1


    w = 1
    while w == 1:
        new_page = input("Do you want to create a new page? [Y, n] ")

        if new_page == 'y' or new_page == 'Y':
            print("Working 1")
            w = 0
        elif new_page == 'n' or new_page == 'N':
            print("working 2")
            w = 0
        else:
            print("Not valid answer.")
            w = 1

    w = 1
        while w == 1:
            new_post = input("Do you want to create a first post? [Y, n] ")

            if new_post == 'y' or new_post == 'Y':
                print("working 1")
                w = 0
            elif new_post == 'n' or new_post == 'N':
                print("working 2")
            else:
                print("Not valid answer")
