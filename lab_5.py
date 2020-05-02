#Govinda KC
#cs 2302 lab 5A 
# Prof: Diego Aguirre
# TA: Manoj Sah
# last modified 11/27/2018

# importing neccessary libraries
import Heap
import random

# This method sorts by the properties of min heap using the relation of parent and child
def heap_sort(heap_list):
    hip = Heap.Heap()
    i = len(heap_list)//2 -1 
    while i >= 0:
        hip.move_down(i, heap_list,len(heap_list))
        i = i-1
    i = len(heap_list) -1
    while i > 0:
        temp = heap_list[0]
        heap_list[0] = heap_list[i]
        heap_list[i] = temp
        hip.move_down(0, heap_list, i)
        i = i-1
# this try and except method is applicable to avoid the code-run obstruction.
try:
    def read_file():
        heap_list =[]
	# open the file and reads
        _file = open('test_file.txt', 'r+')
	# reads the file splitted by comma
        line = _file.read().split(',')
        for num in line:
	# This below appends the num to the list
            heap_list.append(num)
        heap_list = list(map(int, heap_list))
        return heap_list
except:
    print('file not foud, check the file name')

def main():
    # This is for hard coded values
    print('Testing the hard-coded values:')
    hard_list = [7, 43, 35, 23, 75]
    print('\nbefore sorting:', hard_list)
    heap_sort(hard_list)
    print('after sorting:', hard_list)
    # This is for txt file after reading it.
    print('\nTesting by using the text file')
    read_list = read_file()
    print('\nThe list before heap sort:', read_list)
    heap_sort(read_list)
    print('The list after heap sort', read_list)
main()
