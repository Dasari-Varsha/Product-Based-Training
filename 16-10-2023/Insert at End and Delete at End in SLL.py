#Insert the element at End and Delete at End
#output:2->4->6->8->10->
class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
class linked_list:
    def __init__(self):
        self.head=None
    def insertAtEnd(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            curr=self.head
            while(curr.next):
                curr=curr.next
            temp=node(data)
            curr.next=temp
            temp=temp.next
    def deleteAtEnd(self):
        if self.head==None:
            return
        temp=self.head
        while(temp.next.next):
            temp=temp.next
        temp.next=None
        return temp.val
    def traverse(self):
        temp=self.head
        while(temp):#temp!=None
            print(temp.val,end="->")
            temp=temp.next
l=list(map(int,input().split()))#l=[2,4,6,8,10]
obj=linked_list()
for i in l:
    obj.insertAtEnd(i)
obj.deleteAtEnd()
obj.traverse()