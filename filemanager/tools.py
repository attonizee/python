import os
import shutil
import datetime


#Function to create file
def create_file(name, text = None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


#Function to create directory
def create_directory(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Such folder already exist')


#Function list dirs and files
def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


#Function to delete directories and files
def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


#Function to copy files and directories
def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Such folder already exist')
    else:
        shutil.copy(name, new_name)


#Function logs
def save_info(message):
    current_date = datetime.datetime.now()
    result = f'{current_date} - {message}'
    with open('logs.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


#Function change working directory
def change_dir(name):
    if os.path.isdir(name):
        os.chdir(name)
        print(os.getcwd())
    else:
        print('This is not a directory')


if __name__ == '__main__':
    create_file('test.dat')
    create_file('test.dat', 'Hello')
    create_directory('folder2')
    get_list()
    get_list(True)
    delete_file('test.dat')
    delete_file('folder2')
    copy_file('folder1', 'folder_copy')
    copy_file('first.txt', 'second.txt')
    save_info('test')