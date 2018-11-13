def insertion_reverse_run(a):
    length=len(a)
    for i in range(length-2, -1, -1):
        key=a[i]
        j=i+1
        while(j<length and a[j]>key):
            a[j - 1] = a[j]
            j=j+1
        a[j-1]=key
    return(a)

## test
import random

def ifsorted(a):
    return(a==sorted(a, reverse=True))

for i in range(100000):
    nums = random.sample(range(20), 10)
    # print(nums)
    insertion_reverse_run(nums)
    # print(nums)
    if not ifsorted(nums):
        print("ERROR")
        break
print("DONE")