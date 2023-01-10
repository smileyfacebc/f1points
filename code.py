import json
import os

previous_scores_file = "previous_scores.json"


class Constructor:
    def __init__(self, drivers: list, WCC_points: int):
        self.drivers = drivers
        self.WCC_points = WCC_points

    #to make json operable
    def to_dict(self):
        return {'drivers': self.drivers, 'WCC_points': self.WCC_points}



#loading from previous iteration
if os.path.exists(previous_scores_file):
    with open(previous_scores_file, 'r') as loaded_derp:
        imported_data = json.load(loaded_derp)
    #Rebuilding the class dictionary from 'derp.json
    f1_constructors = {name: Constructor(value['drivers'], value['WCC_points']) for name, value in imported_data.items()}
else:
    # F1 teams:
    #this is made if json file doesn't exist
     f1_constructors = {
        'Mercedes': Constructor(['Ham', 'Rus'], 0),
        'Red_Bull': Constructor(['Ver', 'Per'], 0),
        'Ferrari': Constructor(['Lec', 'Sai'], 0),
        'Alpine': Constructor(['Oco', 'Gas'], 0),
        'McLaren': Constructor(['Nor', 'Pia'], 0),
        'Alpha_Romeo': Constructor(['Bot', 'Gua'], 0),
        'Aston_Martin': Constructor(['Alo', 'Str'], 0),
        'Haas': Constructor(['Mag', 'Hul'], 0),
        'Alpha_Tauri': Constructor(['Tsu', 'Dev'], 0),
        'Williams': Constructor(['Alb', 'Sar'], 0)
    }

Points_Position = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#load from text document
with open('race_result.txt', 'r') as results:
    loaded_results = results.read().split()




for driver in list(zip(loaded_results, Points_Position)):
    for constructor_name in f1_constructors:
        if driver[0] in f1_constructors[constructor_name].drivers:
            f1_constructors[constructor_name].WCC_points += driver[1]
            break



#creating the list for teams and their points
for constructor_name, constructor in sorted(f1_constructors.items(), key=lambda name, obj: Constructor.WCC_points, reverse= True):
        print(f'{constructor_name} has {constructor.WCC_points} points')
        #print(f1_constructors.items())
        #sorted_f1 = sorted(f1_constructors.items(), key=lambda x:x[1])
        #sorted_f1_dict = dict(sorted_f1)
        #print(sorted_f1)
        #print(f'{constructor_name} has {sorted(dir(str(constructor.WCC_points)))} points')


#saving the list to json file
with open(previous_scores_file, "w+") as save_data_file:
    json.dump({constructor_name: constructor.to_dict() for constructor_name, constructor in f1_constructors.items()}, save_data_file)

