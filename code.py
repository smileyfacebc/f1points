import json
import os

previous_constructor_score_file = "previous_constructor_score.json"
#new edit
previous_drivers_championship_file = "previous_drivers_championship.json"

class Constructor:
    def __init__(self, drivers: list, WCC_points: int):
        self.drivers = drivers
        self.WCC_points = WCC_points

    #to make json operable
    def to_dict(self):
        return {'drivers': self.drivers, 'WCC_points': self.WCC_points}

#new edit
class Driver:
    def __init__(self, drivers_championship: int):
        self.drivers_championship = drivers_championship
        
    def to_dict(self):
        return {'driver': self.drivers_championship}





#loading from previous iteration
if os.path.exists(previous_constructor_score_file):
    with open(previous_constructor_score_file, 'r') as loaded_derp:
        imported_data = json.load(loaded_derp)

    f1_constructors = {name: Constructor(value['drivers'], value['WCC_points']) for name, value in imported_data.items()}
else:
    # make this

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

#new edit
if os.path.exists(previous_drivers_championship_file):
    with open(previous_drivers_championship_file, 'r')as loaded_drivers:
        imported_drivers_data = json.load(loaded_drivers)

    f1_drivers = {name: Driver(value, value['drivers_championship']) for name, value in imported_drivers_data.items()}
else:
    #make this
    #__________________ Cory, I was trying to have 'lewis Hamilton' = 'Ham' and associate the points from race results. 
    # am I trying to do too much in one step for this program? or is there a better way?
    f1_drivers = {
        'Lewis Hamilton' : Driver('Ham', 0),
        'George Russel' : Driver('Rus', 0),
        'Max Verstappen' : Driver('ver', 0),
        'Sergio Perez' : Driver('Per', 0),
        'Charles Leclerc' : Driver('Rus', 0),
        'Carlos Sainz' : Driver('Sai', 0),
        'Estaban Ocon' : Driver('Oco', 0),
        'Piere Gasly' : Driver('Gas', 0),
        'Lando Norris' : Driver('Nor', 0),
        'Oscar Piastri' : Driver('Pia', 0),
        'Valteri Bottas' : Driver('Bot', 0),
        'Zhou Guanyu' : Driver('Gua', 0),
        'Fernando Alonso' : Driver('Alo', 0),
        'Lance Stroll' : Driver('Str', 0),
        'Kevin Magnussen' : Driver('Mag', 0),
        'Nico Hulkenburg' : Driver('Hul', 0),
        'Yuki Tsunoda' : Driver('Tsu', 0),
        'Nick De Vries' : Driver('Dev', 0),
        'Alexander Albon' : Driver('Alb', 0),
        'Logan Sargent' : Driver('Sar', 0)
    }





#new line
Points_Position = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#load from text document
with open('race_result.txt', 'r') as results:
    loaded_results = results.read().split()




for driver in list(zip(loaded_results, Points_Position)):
    for constructor_name in f1_constructors:
        if driver[0] in f1_constructors[constructor_name].drivers:
            f1_constructors[constructor_name].WCC_points += driver[1]
            break

#new edit
for driver_result in list(zip(loaded_results, Points_Position)):
    for driver_name in f1_drivers:
        if driver_result[0] in  f1_drivers[driver_name].drivers_championship:
            f1_drivers[driver_name].drivers_championship += driver_result[1]
            break




#creating the list for teams and their points
for constructor_name in sorted(f1_constructors, key=lambda name: f1_constructors[name].WCC_points, reverse= True):
        print(f'{constructor_name} has {f1_constructors[constructor_name].WCC_points} points')


for driver_name in sorted(f1_drivers, key=lambda name: f1_drivers[name].drivers_championship, reverse= True):
    print(f'{driver_name} has {f1_drivers[driver_name].drivers_championship} points')


#saving the list to json file
with open(previous_constructor_score_file, "w+") as save_data_file:
    json.dump({constructor_name: constructor.to_dict() for constructor_name, constructor in f1_constructors.items()}, save_data_file)


#WDC points
with open(previous_drivers_championship_file, "w+") as save_driver_championship_file:
    json.dump({driver_name: Driver.to_dict() for driver_name, driver in f1_drivers.items()}, save_driver_championship_file)
