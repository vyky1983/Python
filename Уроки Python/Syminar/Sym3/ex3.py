def func(a=[]):
    b=[]
    b.append(a)
    a.clear()
    return(b)

list_=[[1,2],[3,4]]
print(list_[0][0])