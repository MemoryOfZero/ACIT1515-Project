# Main class for running the selection game. 
# Will load all games from the modules folder and display them in a menu 

import os
import sys
import importlib
import json

loop = True

with open('config.json', 'r') as f:
    module_list = json.load(f)['modules']

while loop == True:

    print('List of games:')
    for index, module in enumerate(module_list):
        print(index, '-', module)
    print('q - quit')

    selection = input('Select a game: ')

    if selection.lower() == 'q':
        loop = False
        break

    try:
        game = importlib.import_module('modules.' + module_list[int(selection)])
        game.start()

    except Exception as e:
        print(e.message, e.args)

print('Ending program')
