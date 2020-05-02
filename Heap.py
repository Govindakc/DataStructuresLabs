# Last modified: 11/27/2018
# Govinda KC
# CS 2302 10:30
# Lab 5 A
#####################################################################################################################

# Class to create he conditions for the heap

class Heap:
    def __init__(self):
	# Initialization of heap array
        self.heap_array = []
    # This method inserts the items from the array list into the heap array.
    def insert(self, k):
        self.heap_array.append(k)
        self.move_up(len(self.heap_array) -1)
    # This method will swap the elements from the last item till we get the properties of  min-heap.
    def move_up(self, node):
        while node >0:
            # Relation to find the parent of the current node_child
            parent_node = (node -1)//2
            # Check if the max heap is present
            if self.heap_array[node] >= self.heap_array[parrent_node]:
                return
            else:
                # swap the elements to meet the property of the min heap
                temp = self.heap_array[node]
                self.heap_array[node] = self.heap_array[parent_node]
                self.heap_array[parent_node] = temp
                node = parent_node
    # This method will swap the elements from the first item in the heap till the min -heap properties are satisfied.
    def move_down(self, node, heap_list, size):
        child_id = (2*node) +1
        element = heap_list[node]
        # This while loop is to find the max
        while child_id < size:
            max_value, max_id = element, -1
            i = 0
            while i < 2 and i + child_id < size:
                if heap_list[i+child_id]>max_value:
                    max_value = heap_list[i+child_id]
                    max_id = i+child_id
                i = i+1
            if max_value == element:
                return 
            # swap the current node index with the max index using a temp.
            temp = heap_list[node]
            heap_list[node]=heap_list[max_id]
            heap_list[max_id] = temp
            node = max_id
            child_id = 2*node +1
    # this method checks if the heap is empty.
    def is_empty(self):
        return len(self.heap_array)==0
