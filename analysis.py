from recorder import *


def analysis():
    while True:
        print('>>>>>> Enter your question (To EXIT, enter 0 <<<<<<')
        q = input('Your question? ')
        if q.isnumeric() and int(q) == 0:
            break
        rec = Recorder()
        q = q.lower()
        if q == 'number of clubs':
            clubs = rec.read_yaml('Club')
            print(f'number of clubs = {len(clubs)}')
        elif q == 'number of students':
            students = rec.read_yaml('Student')
            print(f'number of students = {len(students)}')
        elif q == 'who has the biggest spending':
            registers = rec.read_yaml('Register')
            registers = convert_to_register_objects(registers)
            max_total = 0
            for regID in range(1, len(registers)+1):
                register = registers[regID]
                if max_total < total(register)[0]:
                    max_total = total(register)[0]
                    maxname = total(register)[1]
            print(maxname)

        else:
            print('Sorry, Cashier does not understand your question')


def total(Obj):
    rec = Recorder()
    clubs = rec.read_yaml('Club')
    students = rec.read_yaml('Student')
    student_name = students[Obj.sID]['name'].capitalize()
    item_counter, total_price = 0, 0
    for pID, qty in Obj.cID_qty_dict.items():
        item_counter = item_counter + 1
        price = clubs[pID]['unitprice']
        item_price = qty * price
        total_price = total_price + item_price
        inf = [total_price, student_name]
    return inf
