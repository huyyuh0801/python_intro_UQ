import yaml
import os
from club import *
from student import *
from register import *


class Recorder:
    def __init__(self):
        self.yaml_fnames = {'Club': 'clubs.yaml', 'Student': 'student.yaml', 'Register': 'registrations.yaml'}

    def read_yaml(self, obj_type):
        fpath = self.yaml_fnames[obj_type]
        object_as_dict = {}
        if os.path.exists(fpath):
            # print(f'reading {fpath}...')
            with open(fpath, 'r') as f:
                object_as_dict = yaml.safe_load(f)
        return object_as_dict

    def write_yaml(self, objects):
        sample_key = list(objects.keys())[0]
        sample_obj = objects[sample_key]
        obj_type = type(sample_obj).__name__
        fpath = self.yaml_fnames[obj_type]
        print(f'writing {fpath}...')
        with open(fpath, 'w') as f:
            objects_as_dict = {}
            for ID, e in objects.items():
                objects_as_dict[ID] = e.get_dict()
            yaml.dump(objects_as_dict, f)

    def w_csv(self):
        for obj_type, yaml_fname in self.yaml_fnames.items():
            fpath = yaml_fname.replace('.yaml', '.csv')
            objects = self.read_yaml(obj_type)
            if obj_type == 'Club':
                objects = convert_to_club_objects(objects)
            elif obj_type == 'Student':
                objects = convert_to_student_objects(objects)
            else:
                objects = convert_to_register_objects(objects)
            if len(objects) == 0:
                print(f'NO {obj_type}, thus {fpath} is not printed!')
                return

            any_object = objects[list(objects)[0]]
            if obj_type == 'Register':
                col_names = ['ID'] + list(any_object.get_dict())
            else:
                col_names = list(any_object.get_dict())
            data = []
            data.append(col_names)
            for eID, e in objects.items():
                e_dict = e.get_dict()
                datum = [eID] + [e_dict[col] for col in col_names if col != 'ID']
                datum = [str(i) for i in datum]
                data.append(datum)
            print(f'writing {fpath}...')
            with open(fpath, 'w') as f:
                for datum in data:
                    f.write(','.join(datum) + '\n')

