idx=-1
idx2=-1
import random
array=[]

for x in range(50):
    a =random.randint(0,200)
    array.append(a)

b =random.randint(0,300)


import time
lt1=time.time()
def lin_search(x,y):
    for i in range(len(array)):
        if array[i]==b:
            globals()["idx"]=i
            return True
        else:
            return False

if lin_search(array,b):
    print("Found the random number {} at index {} position".format(b,idx))
else:
    print("The random number {} was not avaiable in the array".format(b))
lt2=time.time()
print("Run time needed for the algorithm of linear search is:",lt2-lt1)


bt1=time.time()
array.sort()
def bin_search(x,y):
    frst_val=0
    lst_val=len(array)-1
    while frst_val<=lst_val:
        mid_val=(frst_val+lst_val)//2
        if array[mid_val]==b:
            globals()["idx2"] = mid_val
            return True
        else:
            if array[mid_val]>b:
                lst_val=mid_val-1
            else:
                frst_val=mid_val+1
    return False


if bin_search(array,b):
    print("Found the random number {} at index {} position".format(b,idx))
else:
    print("The random number {} was not avaiable in the array".format(b))

bt2=time.time()
print("Run time needed for the algorithm of Binary search is:",bt2-bt1)
