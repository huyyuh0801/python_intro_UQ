from recorder import *


class Club:
    def __init__(self, ID, name, quantity, unitprice):
        self.ID = ID
        self.name = name
        self.quantity = quantity
        self.unitprice = unitprice

    def get_dict(self):
        return {'ID': self.ID, 'name': self.name, 'quantity': self.quantity, 'unitprice': self.unitprice}

    def print_creation_msg(self):
        print(f'An object (ID: {self.ID}) of class Club has been created!')


def addclubs():
    rec = Recorder()
    clubs = rec.read_yaml('Club')
    clubs = convert_to_club_objects(clubs)

    while True:
        print('>>>>>>>>>>>Entering club info (To EXIT, enter ID=0)<<<<<<<<<<<<')
        ID = input('Enter the club ID: ')
        if not ID.isnumeric():
            print('Invalid club ID, skipping this club entry')
            continue
        if int(ID) == 0:
            print('BACK to the Menu!')
            break
        ID = int(ID)
        name = input('Enter the club name: ')

        quantity = input('Enter the club quantity: ')
        if quantity.isnumeric():
            quantity = int(quantity)
        else:
            print('Invalid club quantity, skipping this club entry')
            continue
        unitprice = input('Enter the club unit price: ')
        part = unitprice.split('.')
        if len(part) == 2 and part[0].isnumeric() and part[1].isnumeric():
            unitprice = float(unitprice)
        else:
            print('Invalid club unitprice, skipping this club entry')
            continue
        clubs[ID] = Club(ID, name, quantity, unitprice)
        print("Add clubs", ID, "successfully!")
    rec.write_yaml(clubs)


def convert_to_club_objects(clubs_as_dict):
    clubs = {}
    for ID, c_dict in clubs_as_dict.items():
        name, quantity, unitprice = c_dict['name'], c_dict['quantity'], c_dict['unitprice']
        clubs[ID] = Club(ID, name, quantity, unitprice)
    return clubs
