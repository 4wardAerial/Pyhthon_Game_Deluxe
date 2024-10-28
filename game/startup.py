import os.path
import csv

with open('./game/text/menus.csv', mode='r') as csv_menus:
    menus_dialogue = dict(filter(None, csv.reader(csv_menus)))

PATH_TO_SAVE = './save.txt'
save_exists = os.path.isfile(PATH_TO_SAVE)

if save_exists:
    save_file = open(PATH_TO_SAVE, mode='w')
    print(menus_dialogue["EN.file_not_found.error"])
