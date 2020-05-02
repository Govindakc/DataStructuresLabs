# Govinda KC
# CS 2302 10:30 class
# Instructor: Diego Aguirre
# TA: Manoj Saha
# purpose: use of dynamic programming

# importing the function
from Edit_distance import edit_distance
def main():
    str1 = input('Enter the first string \n')
    str2 = input('Enter the second string \n')
    print('The edit distance is obtained as: \n')
    print('first string:', str1)
    print('second string:', str2)
    num_changes = edit_distance(str1, str2)
    print('\nThe num of changes needed to have same strings:', num_changes)

main()

