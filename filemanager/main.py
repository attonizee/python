import sys

from tools import create_file, create_directory, get_list, delete_file, copy_file, save_info, change_dir
from game import game


print('Hello. File manager is ready to work.')

command = None
save_info('Programm started')


while command != 'exit':
   
    command = input('Enter command or exit to end work. Enter help to list commands: ')
    
    if command == 'list':
        get_list()
    elif command == '0':
        name = input('Enter new path: ')
        change_dir(name)
    elif command == '1':
        name = input('Enter file name: ')       
        if name == '':
            print('File name is missing')
            save_info('Error - File name is missing')
        else:
            create_file(name)
            save_info(f'File {name} is created')
    elif command == '2':
        name = input('Enter folder name: ')
        if name == '':
            print('Folder name is missing')
            save_info('Error - Folder name is missing')
        else:
            create_directory(name)
            save_info(f'Folder {name} is created')
    elif command == '3':
        name = input('Enter file or folder name: ')
        if name == '':
            print('File or folder name is missing')
            save_info('Error delete - File or folder name is missing')
        else:
            delete_file(name)
            save_info(f'Deleted {name}')
    elif command == '4':
        name = input('Enter file or folder to copy: ')
        new_name = input('Enter the new destination: ')
        if name == '':
            print('File or folder name is missing')
            save_info('Error copy - File or folder name is missing')
        else:
            try:
                copy_file(name, new_name)
            except FileNotFoundError:
                print('New destination is missing')
                save_info('Error copy - New destination is missing')
            else:
                copy_file(name, new_name)
                save_info(f'Succes copy. From {name} to {new_name}')
    elif command == '5':
        game()
    elif command == 'help':
        print('list - show files and folders')
        print('0 - change working directory')
        print('1 - create file')
        print('2 - create folder')
        print('3 - delete file or folder')
        print('4 - copy file or folder')
        print('5 - play game guess number')

print('Log out')
save_info('Programm terminated')


