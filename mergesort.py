def merge(d,left,right,mid):
    if left==mid==right:
        return
    a=[0]*(mid-left+1)
    b=[0]*(right-mid)
    for i in range(0,mid-left+1):
        a[i]=d[i+left]
    for i in range(0,right-mid):
        b[i]=d[i+mid+1]
    k=left
    j=0
    for i in range(0,len(a)):
        while j < len(b) and a[i] > b[j]:
            d[k]=b[j]
            j=j+1
            k=k+1
        d[k]=a[i]
        k=k+1
    while j < len(b) :
        d[k]=b[j]
        j=j+1
        k=k+1
#####################################################

def mergesort(a,left,right):
    mid=left + round((right - left)/2)
    if right==left:
        return
    elif (right-left)==1:
        merge(a, left, right, mid)
    else:
        mergesort(a,left,mid)
        mergesort(a,mid+1,right)
    merge(a,left,right,mid)