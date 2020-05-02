# Govinda kc
# CS 2302
# Lab 7A
# purpose: use of dynamic programming

# defining the function

def edit_distance (str1, str2):
    # creating a 2D array using the strings provided
    new_table = [[0 for i in range(len(str1)+1)] for j in range(len(str2)+1)]
    
    # Filling the first line and column as follows
    for i in range(len(str1)+1):
        new_table[0][i] = i
    for i in range(len(str2)+1):
        new_table[i][0] = i
   # Nested loop that used for the number of changes we need to make
    for i in range(len(str2)):
        for j in range(len(str1)):
           # Use the diagonal value if the characters on the both the strings are same.
            if str1[j] == str2[i]:
                new_table[i+1][j+1] = new_table [i][j]
            # Add 1 to the smallest value if the characters on the both strings are different.
            else:
                new_table[i+1][j+1] = min(new_table[i][j], new_table[i][j+1], new_table[i+1][j])+1
    # Total number of the changes in the total code is given as:
    num_changes = new_table[len(str2)][len(str1)]
    return num_changes
   
