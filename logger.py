#!/usr/bin/env 
# logger.py

import subprocess

def get_processes():
    processes = subprocess.run(
        'wmic process get description,executablepath'.split(' '), 
        stdout=subprocess.PIPE)
    # Seperate lines into list and remove spaces inbetween items
    processes = str(processes).split('\\r\\r\\n')
    processes = [p.split('  ') for p in processes]
    # Clean up list
    process_list = []
    for process in processes:
        process = [p.strip() for p in process] # Remove straggling spaces
        process_list.append( list(filter(None, process)) ) # Remove empties 
    process_list = process_list[3:-2] # Remove more junk
    # Clean up strings
    for i, p in enumerate(process_list):
        # print(p)
        if len(p) == 0:
            process_list.pop(i)
        elif not p[0].lower().endswith('.exe'):
            process_list.pop(i)
        elif len(p) > 1:
            p[1] = p[1].replace('\\'*4,'\\')
            p[1] = p[1].replace('.EXE','.exe')
    # Remove dublicate/similar processes, ie: steamwebhelper.exe = steam.exe
    for p in process_list:
        ammount = process_list.count(p)
        if ammount > 1:
            for i in range(ammount-1): process_list.remove(p)

    for x in process_list:
        print(x)
    print('')
    # with open('process_list.txt', 'w') as file:
    #     for x in process_list:
    #         file.write(str(x) + '\n')
    return process_list


    
def main():
    processes = get_processes()
    sl = '\\'*4
    steam_dir = 'C:{sl}Program Files (x86){sl}Steam{sl}steamapps{sl}common'
    running_games = []
    for p in processes:
        if len(p) > 1 and p[1] == steam_dir:
            running_games.append(p)
    for x in running_games:
        print(x)

if __name__ == '__main__':
    import os, sys
    main()
