# Govinda KC
# CS 2302 lab2
# import sys to increase the recursion limit.
import sys

sys.setrecursionlimit(6500)

# Define class to create nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating the class for linked list
class LinkedList:
    def __init__(self):
        self.head = None

# method to print the linked list
    def printList(self,n=-1):
        temp = self.head
        count = 0
        while temp:
            if count == n:
                break
            print(temp.data)
            temp = temp.next
            count+=1

# Defining the method to create a node at the end of the linked list
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
# reading files
def read_file(filename):
    text_file = open(filename, 'r')
    l_list = text_file.read().splitlines()
    return l_list

# Creating the linked list of the one single file
def get_linked_list(a_list):
    list1 = LinkedList()
    for i in range(len(a_list)):
        list1.append(int(a_list[i])) # use float if you have floating num
    return list1

# Defining function which will merge two linked lists
def mergeLists(list1, list2):
    temp = None
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    if list1.data <= list2.data:
        temp = list1
        temp.next = mergeLists(list1.next, list2)
    else:
        temp = list2
        temp.next = mergeLists(list1, list2.next)
    return temp

# Solution 3
# Defining function which will sort the linked list using mergeSort
def mergeSort(head):
    if head is None or head.next is None:
        return head

    list1, list2 = divideLists(head)
    list1 = mergeSort(list1)
    list2 = mergeSort(list2)
    head = mergeLists(list1, list2)
    return head

# Defining function which will divide a linked list into two equal linked lists
def divideLists(head):
    slow = head                     # slow is a pointer to reach the mid of linked list
    fast = head                     # fast is a pointer to reach the end of the linked list
    if fast:
        fast = fast.next            
    while fast:
        fast = fast.next            # fast is increased by 2 times than slow.
        if fast:
            fast = fast.next
            slow = slow.next
    mid = slow.next
    slow.next = None
    return head, mid
# Solution 2
def bubbleSort(head):
    if head is None or head.next is None:
        return head
    else:
        sorted = False
        while not sorted:
            sorted = True
            prev = head
            current = head.next
            while current!=None:
                if prev.data > current.data:
                    sorted = False
                    temp = current.data
                    current.data = prev.data
                    prev.data = temp
                prev = current
                current = current.next
    return head

def count_sorted(head):
    if head is None:
        return 0
    elif head.next is None:
        return 1
    duplicates = 0
    temp = []
    current = head
    while current.next != None:
        next = current.next
        if next.data == current.data:
            temp.append(current.data)
            duplicates += 1
        current = current.next
    temp.sort()
    print("Number of duplicates = "+str(duplicates))

# Solution 1
def count_nested(head):
    if head is None:
        return 0
    elif head.next is None:
        return 1
    duplicates = 0
    temp = []
    current1 = head
    while current1 !=None:
        #data = head.data
        data = current1.data
        current2 = current1.next

        while current2!=None:
            if current2.data == data:
                temp.append(data)
                duplicates += 1
            current2 = current2.next
        current1 = current1.next

    temp.sort()
    print(temp)
    print("Number of duplicates = " + str(duplicates))

# Solution 4
def seen(head):
    numDuplicates = 0
    numComparisions = 0
    seenBefore = [False]*6001
    temp = head
    list1=[]
    while temp is not None:
        numComparisions +=1
        if seenBefore[temp.data] ==True:
            numDuplicates +=1
            list1.append(True)
        else:
            list1.append(False)
            seenBefore[temp.data] = True
        temp = temp.next
    print(list1)
    return {numComparisions, numDuplicates}
# Main logic
if __name__ == '__main__':
    a_list = read_file('activision.txt')
    v_list = read_file('vivendi.txt')

    a_list.extend(v_list)

    list = get_linked_list(a_list)

    #print("Linked list before sorting")
    #list.printList()
    #list.head = bubbleSort(list.head) # Applying bubbleSort to linked list

    #list.head = mergeSort(list.head) # Applying mergeSort to linked list
    #print("Linked list after sorting")
    #list.printList()
    #print('-----------')
    #count_sorted(list.head)
    count_nested(list.head)

    #out1, out2=seen(list.head)
    #print(out1, out2)
