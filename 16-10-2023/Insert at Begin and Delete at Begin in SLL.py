#Insert the element at Begin and Delete at Begin
class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
class linked_list:
    def __init__(self):
        self.head=None
    def insertAtBegin(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            temp=node(data)
            temp.next=self.head
            self.head=temp
    def deleteAtBegin(self):
        if self.head==None:
            return
        temp=self.head
        self.head=self.head.next
        temp.next=None
        return temp.val
        
    def traverse(self):
        temp=self.head
        while(temp):#temp!=None
            print(temp.val,end="->")
            temp=temp.next
l=[2,4,6,8,10]
obj=linked_list()
for i in l:
    obj.insertAtBegin(i)
print(obj.deleteAtBegin())
obj.traverse()