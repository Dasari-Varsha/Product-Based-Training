#DOUBLE LINKED LIST
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert_begin(self,data):
        if self.head==None:
            self.head=node(data)
        else :
            temp=node(data)
            temp.right=self.head
            self.head.left=temp
            self.head=temp
    def insert_end(self,data):
        if self.head==None:
            self.head=node(data)
        else :
            temp=self.head
            new=node(data)
            while temp.right!=None:
                temp=temp.right
            temp.right=new
            new.left=temp
    def del_first(self):
        temp=self.head
        self.head=temp.right
    def del_end(self):
        temp=self.head
        temp1=temp.right
        while temp1.right!=None:
            temp=temp.right
            temp1=temp1.right
        temp.right=None
    def traverse(self):
        temp=self.head.right
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.right
    def reverse(self):
        curr=self.head
        while curr:
            curr.left,curr.right=curr.right,curr.left
            curr=curr.left
        self.head,self.tail=self.tail,self.head
obj=dll()
l=[5,4,3,2,1]
for i in l:
    obj.insert_begin(i)
    #print(obj.data)
obj.traverse()
print()
obj.insert_end(100)
obj.traverse()
print()
obj.del_first()
obj.traverse()
print()
obj.del_end()
obj.traverse()
obj.reverse()
print()