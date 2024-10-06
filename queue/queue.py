class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class Queue:
    def __init__(self,value):
        new_node=Node

        self.first=new_node
        self.last=new_node
        self.length=1


    def print_queue(self):
        temp=self.first
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def enqueue(self,value):
        new_node=Node
        self.last.next=new_node
        self.last=new_node
        self.length+=1

    def dequeue(self,value):
        if self.length==0:
            return None
        temp=self.first
        self.first=self.first.next
        temp.next=None
        self.length-=1    


my_queue=Queue(4)
