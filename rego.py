from analysis import *
from writecsv import *
from club import *
from student import *
from register import *
# (Functionality 0) Menu display and selection
while True:
    print("#" * 60)
    print("THE REGO APP: MENU")
    print("[1] Add clubs")
    print("[2] Add students")
    print("[3] Register")
    print("[4] Print CSV")
    print("[5] Interactive analysis")
    print()
    n = float(input("Menu choice (To Exit, enter 0): "))
    if n == 1:
        addclubs()
    elif n == 2:
        add_students()
    elif n == 3:
        registered()
    elif n == 4:
        writecsv()
    elif n == 5:
        analysis()
    elif n == 0:
        print("The Rego App is existing... Bye!")
        break
    else:
        print("Unknown menu selection: BACK to the menu")
