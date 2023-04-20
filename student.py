from recorder import *


class Student:
    def __init__(self, ID, name, dob, suburb):
        self.ID = ID
        self.name = name
        self.dob = dob
        self.suburb = suburb

    def get_dict(self):
        return {'ID': self.ID, 'name': self.name, 'dob': self.dob, 'suburb': self.suburb}

    def print_creation_msg(self):
        print(f'An object (ID: {self.ID}) of class Student has been created!')


def is_valid_dob_string(dob_str):
    parts = dob_str.split('/')
    if len(parts) != 3:
        return False
    for p in parts:
        if not p.isnumeric():
            return False
    if not (1 <= int(parts[0]) <= 31):
        return False
    if not (1 <= int(parts[1]) <= 12):
        return False
    if not (1900 <= int(parts[2]) <= 2100):
        return False
    return True


# student.py


def add_students():
    rec = Recorder()
    students = rec.read_yaml('Student')
    students = convert_to_student_objects(students)

    while True:
        print('>>>>>>>>>Entering student info (To EXIT, enter ID = 0)<<<<<<<<<<<<')
        ID = input('Enter the student ID: ')
        ID = int(ID)
        if ID == 0:
            print('Back to the Menu!')
            break
        name = input('Enter the student name: ')
        dob = input('Enter the student DOB (dd/mm/yyyy): ')
        if not is_valid_dob_string(dob):
            print('Invalid DOB format, skipping this student entry! ')
            continue

        suburb = input('Enter the student suburb: ')
        students[ID] = Student(ID, name, dob, suburb)

    rec.write_yaml(students)


def convert_to_student_objects(students_as_dict):
    students = {}
    for ID, c_dict in students_as_dict.items():
        name, dob, suburb = c_dict['name'], c_dict['dob'], c_dict['suburb']
        students[ID] = Student(ID, name, dob, suburb)
    return students
