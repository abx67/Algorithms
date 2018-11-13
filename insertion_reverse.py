def insertion_reverse(a):
    length=len(a)
    for i in range(1,length):
        key=a[i]
        j=i-1
        while(j>=0 and a[j]<key):
            a[j + 1] = a[j]
            j=j-1
        a[j+1]=key
    return(a)

## test
import random

def ifsorted(a):
    return(a==sorted(a, reverse=True))

nums = random.sample(range(20), 10)
print(nums)
insertion_reverse(nums)
print(nums)
print(ifsorted(nums))