# Govinda KC
# CS 2302 10:30 am class
# Lab 1

import os
import random


def get_dirs_and_files(path):

    dir_list = [path + '/' + directory for directory in os.listdir(path) if os.path.isdir(path + '/' + directory)]
    file_list = [path+ '/' + directory for directory in os.listdir(path) if not os.path.isdir(path + '/' + directory)]

    return dir_list, file_list


def classify_pic(path):
    if "dog" in path:
        return 0.5 + random.random() / 2

    return random.random() / 2


def process_dir(path):
    path = os.path.abspath(path)
    cat_list = []
    dog_list = []
    dir_list, file_list = get_dirs_and_files(path)
    dir_list = [os.path.abspath(d) for d in dir_list]
    file_list = [os.path.abspath(f) for f in file_list]
    #print(dir_list, file_list)
    for _file in file_list:
        if classify_pic(_file) > 0.5:
            dog_list.append(_file)
        elif 'cat' in _file:
            cat_list.append(_file)
    if len(dir_list) > 0:
        for _dir in dir_list:
            #print(_dir)
            new_cats, new_dogs = process_dir(_dir)
            cat_list.extend(new_cats)
            dog_list.extend(new_dogs)
    return cat_list, dog_list


def main():
    start_path = './' # current directory

    cats, dogs = process_dir(start_path)
    print("CATS_list: ", cats)
    print()
    print("DOGS_list: ", dogs)

main()