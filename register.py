import datetime
from club import convert_to_club_objects
from student import convert_to_student_objects
from recorder import *


def registered():
    rec = Recorder()
    students = rec.read_yaml('Student')
    students = convert_to_student_objects(students)
    clubs = rec.read_yaml('Club')
    clubs = convert_to_club_objects(clubs)
    registers = rec.read_yaml('Register')
    registers = convert_to_register_objects(registers)

    while True:
        print('>>>>> Entering a student ID (To EXIT, enter student ID=0)<<<<<')
        sID = input('Enter your student ID: ')
        sID = int(sID)
        if sID == 0:
            print('Back to the Menu!')
            return
        if sID in students:
            break
        else:
            print('Your ID is not registered')

    cID_qty_dict = {}
    while True:
        print('>>>>>Entering an item(To EXIT, enter club ID = 0)<<<<<<')
        pID = input('Entering the club ID: ')
        pID = int(pID)
        if pID == 0:
            print('Back to the Menu!')
            break
        if pID not in clubs:
            print('Unknown club ID!')
            continue
        quantity = input('Enter the club quantity: ')
        if quantity.isnumeric():
            quantity = int(quantity)
        else:
            print('Invalid club quantity, skipping this entry')
            continue
        if quantity >= clubs[pID].quantity:
            print('Not enough availability on this club')
            continue
        else:
            clubs[pID].quantity = clubs[pID].quantity - quantity
        cID_qty_dict[pID] = quantity

    if len(registers) == 0:
        regID = 1
    else:
        keys = []
        for k in registers.keys():
            keys.append(k)
        keys = sorted(keys)
        last_regID = keys[-1]
        regID = last_regID + 1
    register = Register(regID, sID, cID_qty_dict)
    register.print_receipt_str()
    registers[regID] = register

    rec.write_yaml(registers)
    rec.write_yaml(clubs)


class Register:
    def __init__(self, regID, sID, cID_qty_dict):
        time = datetime.datetime.now()
        self.timestamp = time.strftime("%d/%m/%Y at %H:%M:%S")
        self.cID_qty_dict = cID_qty_dict
        self.sID = sID
        self.regID = regID

    def get_dict(self):
        return {'sID': self.sID, 'cID_qty_dict': self.cID_qty_dict}

    def print_receipt_str(self):
        receipt_str = self.make_receipt_str()
        with open('receipt.txt', 'w') as f:
            f.write(receipt_str)

    def make_receipt_str(self):
        rec = Recorder()
        clubs = rec.read_yaml('Club')
        students = rec.read_yaml('Student')
        student_name = students[self.sID]['name'].capitalize()
        item_counter, total_price = 0, 0

        receipt_strs = [f'############ Receipt {self.regID} ###########', 'School XYZ', self.timestamp + '\n']
        for pID, qty in self.cID_qty_dict.items():
            item_counter = item_counter + 1
            name = clubs[pID]['name']
            price = clubs[pID]['unitprice']
            item_price = qty * price
            total_price = total_price + item_price
            receipt_strs.append(f'Item {item_counter}: {name}')
            receipt_strs.append(f'{qty}*{price} AUD = \t {item_price} AUD')
        receipt_strs.append('---------------------------')
        receipt_strs.append(f'TOTAL \t \t {total_price} AUD')
        receipt_strs.append(f'############## Thank you, {student_name} ###########')

        receipt_strs = '\n'.join(receipt_strs)
        return receipt_strs


def convert_to_register_objects(register_as_dict):
    registers = {}
    for regID, c_dict in register_as_dict.items():
        sID, cID_qty_dict = c_dict['sID'], c_dict['cID_qty_dict']
        registers[regID] = Register(regID, sID, cID_qty_dict)
    return registers
