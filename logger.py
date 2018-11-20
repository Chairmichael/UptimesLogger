#!/usr/bin/env 
# logger.py

import subprocess

def main():
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
    for i, p in enumerate(process_list):
        if p in unique_processes:
            del process_list[i]
        else:
            unique_processes.append(p)

    for x in process_list:
        print(x)
    with open('process_list.txt', 'w') as file:
        for x in process_list:
            file.write(str(x) + '\n')

if __name__ == '__main__':
    import os, sys
    main()
