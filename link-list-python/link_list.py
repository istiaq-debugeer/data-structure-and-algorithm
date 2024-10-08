class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

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
            self.tail=new_node
        self.length+=1
        return True    
    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1  
    
    def pop_list(self,value):
        if self.length==0:
           return None
        else:
            temp=self.head
            pre=self.head

            while (temp.next) :
                pre=temp
                temp=temp.next
                self.tail=pre
                self.tail.next=None

            self.length-=1

    def insert(self,index,value):
        pass
    
    def pop_first(self):
        if self.length==0:
            return None
        else:
         temp=self.head
         self.head=self.head.next
         temp.next=None
         self.length -=1
        
    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp    
    

