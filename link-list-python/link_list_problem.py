# write a method to find middle node and return the middle node in the Linked list without using diffarent length attribute
from link_list import Node,LinkList

def find_middle_node(self):
    slow=self.head
    fast=self.head
    while fast is not None and fast.next is not None:
        slow=slow.next
        fast=fast.next.next
    return slow    

# LL: Has Loop 
# Write a method called has_loop that is part of the linked list class.

# The method should be able to detect if there is a cycle or loop present in the linked list.

# The method should utilize Floyd's cycle-finding algorithm, also known as the "tortoise and hare" algorithm, to determine the presence of a loop efficiently.

# The method should follow these guidelines:

def has_loop(self):
    slow=self.head
    fast=self.head

    while fast is not None and fast.next is not None:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
        return False

# Instructions:
# LL: Remove Duplicates 
# You are given a singly linked list that contains integer values, where some of these values may be duplicated.
# Your task is to implement a method called remove_duplicates() within the LinkedList class that removes all duplicate values from the list.
# Your method should not create a new list, but rather modify the existing list in-place, preserving the relative order of the nodes.
# You can implement the remove_duplicates() method in two different ways:


def remove_duplicates(self):
    values=set()
    previous=None

    current=self.head

    while current:
        if current.value in values:
            previous.next=current.next
            self.length-=1
        else:
            values.add(current.value)
            previous=current
        current=current.next        

# Instructions:
# LL: Reverse Between
# You are given a singly linked list and two integers m and n. Your task is to write a method reverse_between within the LinkedList class that reverses the nodes of the linked list from index m to index n (inclusive) in one pass and in-place.
# Input
# The method reverse_between takes two integer inputs m and n.
# The method will only be passed valid indexes (you do not need to test whether the indexes are out of bounds)
# Output
# The method should modify the linked list in-place by reversing the nodes from index m to index n.
# If the linked list is empty or has only one node, the method should return None.

# Example
# Suppose the linked list is 1 -> 2 -> 3 -> 4 -> 5, and m = 2 and n = 4. Then, the method should modify the linked list to 1 -> 2 -> 5 -> 4 -> 3 .

def reverse_ll(self,m,n):
    if not self.head:
        return None
    
    dummy=Node(0)
    dummy.next=self.head
    prev=dummy
    current=prev.next
    for i in range(n-m):
        temp=current.next
        current.next=temp.next
        temp.next=prev.next
        prev.next=temp
    self.head=dummy.next

 

