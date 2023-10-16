#Creating the nodes in linked list
class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
obj1=node(1)
obj2=node(2)#obj1.next=node(2)
obj3=node(3)#obj1..next.next=node(3)
obj1.next=obj2
obj2.next=obj3
print(obj1,obj1.val,obj1.next)
print(obj2,obj2.val,obj2.next)
