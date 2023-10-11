#merge two lists removing duplicate elements
def merge(list1,list2):
    t=list1[:]
    for i in list2:
        if i not in t:
            t.append(i)
    return t
list1=[1,2,3,4,5]
list2=[2,3,4,5,6,7,8,9]
res=merge(list1,list2)
print(res)