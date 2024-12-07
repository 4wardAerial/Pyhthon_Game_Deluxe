from pathlib import Path
import os.path
import csv

LANGUAGE = 'BR.'
PATH_TO_MENUS = Path('game/text/menus.csv')
PATH_TO_SAVE = Path('save/save.txt')

# Opens CSV file to get the menu dialogues
with open(PATH_TO_MENUS, mode='r', encoding='utf-8') as csv_menus:
    menus_dialogue = dict(filter(None, csv.reader(csv_menus)))

def menus_csv_handle():
    menus_csv_exists = os.path.isfile(PATH_TO_MENUS)

    if not menus_csv_exists:
        if LANGUAGE == 'EN.':
            print("FATAL ERROR :: 'MENUS.CSV' FILE NOT FOUND :: PLEASE DOWNLOAD THE GAME AGAIN")
        elif LANGUAGE == 'BR.':
            print("ERRO FATAL :: ARQUIVO 'MENUS.CSV' NÃO ENCONTRADO :: POR FAVOR INSTALE O JOGO NOVAMENTE")
        
        quit()

def save_file_handle():
    save_exists = os.path.isfile(PATH_TO_SAVE)


    if save_exists:
        save_file = open(PATH_TO_SAVE, mode='w')

    else:
        print(menus_dialogue[LANGUAGE + "save_file_not_found.error"])

