# Part 1 - Linear Search

def linear_search(nums, value):
    for i in range(len(nums)):
        if nums[i] == value:
            return i


# index 0  1  2  3  4  5  6  7
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# index = linear_search(nums, 3)
# print(index)  # 2


##################################
# Part 2 - Binary Search

def binary_search(nums, value):
    # define the indices
    low = nums[0]
    high = nums[-1]
    # loop while low is less than high
    while low < high:
        # calculate the middle index
        middle = high // 2
        # return if the middle element is the target
        if middle == value:
            return middle
        # if the target is less than the mid, make high equal to middle
        elif value < middle:
            high = middle
            # and loop again
            continue
        # if the target is greater than the mid, make low equal to middle
        elif value > middle:
            low = middle
            # and loop again
            continue
        # if the value was not found
        else:
            return None


      # 0  1  2  3  4  5  6  7
nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = binary_search(nums, 3)
print(index)  # 2

#####################################################
# Part 3 - Bubble Sort


# def bubble_sort(nums):


#       0  1  2  3  4  5  6  7
# nums = [4, 1, 8, 7, 5, 2, 6, 3]

#####################################################
# Part 4 - Insertion Sort

# def insertion_sort(nums):
#     i = 1
#     while i < len(nums):
#         j = i
#         while j > 0 and nums[j-i] > nums[j]:

###############################################
#  Part 1: Stack

# class Node:
#   # used for new root nodes
#   #
#     def __init__(self, item, next=None):
#         self.item = item
#         self.next = next

#     def __str__(self):
#         return f'({self.item}, {self.next})'


# class Stack:
#     def __init__(self):
#       # the root is the top of the stack
#         self.root = None

#     def push(self, element):  # insert an element at the start (new root)
#       if self.root is None:  # check if the stack is empty
#         # if empty, create a new root node; the item is element, and the next is None
#         self.root = Node(element, None)
#       else:
#         # if the stack is not empty, make a new node pointing to the old root, which is now second on the stack
#         node = Node(element, self.root)
#         # the newly-created node is now at the top of the stack(the root)
#         self.root = node

#     def pop(self):  # remove an element from the start (the root becomes the next node)
#       # if the stack is empty, return None. We can't remove something from nothing
#       # if empty, do nothing
#         if self.root is None:
#           return None
#         else:
#           # the new root is now the former next, and new next is the former 3rd

#           self.root = Node(self, None)

#         # temp = head
#         # head = head.next
#         # delete temp

#     def peek(self):  # returns the element on the root node or None if there is no root
#         ...

#     def length(self):  # return the number of elements
#         ...


#      def __str__(self):
#         output = ''
#         n = self.root
#         while n is not None:
#             output += f'({n.item},{n.next is not None}) '
#             n = n.next
#         return output


# s = Stack()
# s.push(5)
# s.push(6)
# print(s.length())  # 2
# print(s.pop())  # 6
# print(s.pop())  # 5
