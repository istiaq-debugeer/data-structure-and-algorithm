class Node():

    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None


class LinkList:

    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1

    def  pop(self,value):
        temp=self.tail
        self.tail=self.tail.prev
        self.tail.next=None
        temp.prev=None
        self.lengh -=1

    def prepend(self,value):
        new_node=Node(value)
        
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node

        






