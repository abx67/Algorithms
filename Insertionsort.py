def insertion(a):
    length=len(a)
    for i in range(1,length):
        key=a[i]
        j=i-1
        while(j>=0 and a[j]>key):
            a[j + 1] = a[j]
            j=j-1
        a[j+1]=key
    return(a)
