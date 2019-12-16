Q1
def rpl_all(dict, m, n):
    for i in dict:
        if dict[i] == m:
            dict[i]=n


d = {'f': 2, 'b': 3, 'g': 3, 'xy': 99}
rpl_all (d, 3, 'poof')


print(d == {'f': 2, 'b': 'poof', 'g': 'poof', 'xy': 99})

Q2
def freq(L):
    a={}
    
    for i in range(0,len(L)):
        count=1
        
        if L[i] in a:
            continue
        for t in range (i+1,len(L)):
            if L[i]==L[t]:
                count+=1
        a[L[i]]=count
    
    return a


print(freq (['the', 'name', 'of','the','of','name','of','song']))


Q3
def mst_freq(lst):
    a={}
    
    for i in range(0,len(lst)):
        count=1
        
        if lst[i] in a:
            continue
        for t in range (i+1,len(lst)):
            if lst[i]==lst[t]:
                count+=1
        a[lst[i]]=count
    key,max=a.popitem()
    for i in a:
        if max<a[i]:
            max=a[i]
            key=i

return key



lst = [1, 4, 2,6,6,6,6 ,4,5,5,5]
print(mst_freq (lst))

Q4
def containsDuplicates(L):
    for i in reversed(L):
        L.pop()
        if i in L:
            return True
    return False

a=[1,2,3,4,5,6]
print(containsDuplicates(a))

Q5
def common_keys(D0,D1):
    newdic={}
    for key in D0.keys():
        print(key)
        if key in D1.keys():
            newdic[key]=(D0[key],D1[key])
    return(newdic)
a={1:1,2:1,3:2,5:1,6:1}
b={1:1,2:1,3:4}

print (common_keys(a,b))

Q6
def rm_first (lst, elm):
    
    if lst[0]==elm:
        lst.pop(0)
        return lst
    return rm_first
print(rm_first ([3, 4,3] , 3))

Q7
def rm_first(lst):
    if len(lst) == 0:
        return lst
    pivot = lst[0]
    pivots = [x for x in lst if x == pivot]
    small = rm_first([x for x in lst if x < pivot])
    large = rm_first([x for x in lst if x > pivot])
    return small + pivots + large
print(rm_first ([6,2,1,5]))

