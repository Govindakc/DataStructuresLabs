# Govinda KC
# CS 2302 10:30 am class
# Lab 1

import os
import random


def get_dirs_and_files(path):
    #print(path)
    #exit()
    dir_list = [path + '/' + directory for directory in os.listdir(path) if os.path.isdir(path + '/' + directory)]
    file_list = [path+ '/' + directory for directory in os.listdir(path) if not os.path.isdir(path + '/' + directory)]
    #print(dir_list)
    #print(file_list)
    #exit()
    return dir_list, file_list


def classify_pic(path):
    # To be implemented by Diego: Replace with ML model
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

=======
#####################################################################################################
# Govinda KC                                                                                        #
# CS2302 Lab 3                                                                                      #
# Instructur: Diego Aguirre                                                                         #
# TA : Manoj Shah                                                                                   #
#####################################################################################################
# The purpose of this lab is to find the relationship between the pair of words interms of cosine similarity.
# The value of cosine angle is from -1 to 1. The value close to 1 tells that words pair is highly related to 
# each other while close to -1 means that they are completely opposite to each other.. 

# Importing the required Modules.
import math
import AVLTree
import RedBlackTree
from AVLTree import AVLTree
from RedBlackTree import RedBlackTree
from AVLTree import Node

# Function to read a given file.
def read_file():
    f = open('glove.6B.50d.txt', encoding="utf-8")
    line = f.readline()
# Creating the array, embedding and node.
    while line:
    # Splitting the line
        _line = line.split(" ")
        # Checking if the first letter is an alphabet.
        word = _line[0]
        if word[0].isalpha():
            # initializing the array as an null.
            embedding_array = []
            for j in range(1,len(_line)):
                embedding_array.append(float(_line[j]))
            node = Node(word, embedding_array)
            # Using try and Except to insert the word in node
            try:
                tree.insert(node)
            except:
                tree.insert(word,embedding_array)
            # Go to next line
        line = f.readline()
    f.close()

# Give the options to user RedBlack or AVL Tree? 
while True:
    _input = input("Type 0 for Red-black tree and 1 for AVL tree: ")
    if _input is not '0' and _input is not '1':
        print("Wrong input" )
        continue
    else:
        break
# This is for RedBlackTree when user chose 0
if _input is "0":
    tree = RedBlackTree()
    # Function will be called to read the file.
    read_file()
    # This line prints the nodes count and height in total
    print("RedBlack Tree has "+ str(len(tree)) + ' nodes')
    print('and')
    print("It's height is " + str(tree._height()))

    # Writing all the words into a single file
    output_file = open("RedBlack_tree.txt", "w+", encoding = 'utf-8')
    tree._write()
    output_file.close()
    
    # Gives the depth of nodes of user's choice.
    while True:
        _inputuser = input("Please enter the depth of nodes you would like printed to file: ")
        # Checks if the input is valid for the tree.
        if int(_inputuser) >= int(tree._height()) or int(_inputuser) < 0:
             print("Depth is not valid, please choose another depth size" )
             continue
        else:
             break

    # Creating file for depth
    k=int(_inputuser)
    depth_file = open("RB_depth.txt", "w+", encoding="utf-8")
    #k=int(_inputuser)
    tree._depth(k)
    depth_file.close()
    print('******************************************************************************************')

# This is for AVL Tree  when user chose 1
if _input is "1": 
    tree = AVLTree()
    read_file() 
    # This line prints the nodes count and height in total
	
    print("AVL Tree has "+ str(tree._size())+' nodes')
    print('and')
    print("It's height is " + str(tree._height()))
    
    # Writing all the words into a single file
    output_file = open("AVL_tree.txt", "w+", encoding = 'utf-8')
    tree._write()
    output_file.close()
    
    # For depth
    while True:
        _inputuser = input("Please enter the depth of nodes you would like printed to file: ")
        print()
        # Checks if the input is valid for the tree.
        if int(_inputuser) >= int(tree._height()) or int(_inputuser) < 0:
            print("Depth is not valid, please choose another depth size: ")
            continue
        else:
             break

    # Creating file for depth
    k=int(_inputuser)
    depth_file = open("AVL_depth.txt", "w+", encoding = 'utf-8')
    tree._depth(k)
    depth_file.close()
# Read the given file to find the relations of the words interms of cosine similarity.
f = open('appendix.txt')
line = f.readline()

# Cosine similarity calculations
while line:
    # spliting the line and creating array
    _line = line.split(" ")
    # searching and assigning the nodes
    w0 = tree.search(_line[0])
    w1 = tree.search(_line[1])
    if w0 is None or w1 is None:
        print('no comparison is found')
        # This section computes the angle of similarity between the two words using dot product and magnitudes
    else:
    # Now Measure the cosine similarity angle between two words.
    # Initialization of terms
        dot_prod = 0
        magnitude_0 = 0
        magnitude_1 = 0
        e0 = w0.get_embedding()
        e1 = w1.get_embedding()
        for i in range (len(e0)):
            # dot product between two embedding vectors
            dot_prod+= e0[i]*e1[i]
            magnitude_0 += e0[i]*e0[i]
            magnitude_1 += e1[i]*e1[i]
        magnitude_0 = math.sqrt(magnitude_0)
        magnitude_1 = math.sqrt(magnitude_1)
        magnitude_0 = magnitude_0 * magnitude_1
        # Relation for cosine similarity measurement
        cosine_similarity = dot_prod/magnitude_0
        print(_line[0],"",_line[1],"", cosine_similarity)
    line = f.readline()
>>>>>>> CS2302_Lab3/master
