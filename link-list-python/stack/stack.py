from link_list import Node

class Stack:
    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node
        self.bottom=new_node
        self.height=1

    def print_stack(self):
        temp=self.top
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def push_stack(self,value):
          new_node=Node(value)
          if self.height==0:
            self.top=new_node
          else:
              new_node.next=self.top
              self.top=new_node
          self.height+=1    
              
    def pop(self,value):
        temp=self.top
        if temp is None:
            return False          
        else:
            self.top=self.top.next
            temp.next=None
        self.length-=1  