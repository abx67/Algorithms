def Partition(A,left,right):
    split=0
    pivot=A[right]
    print("pivot",pivot)
    for i in range(left,right+1):
        if A[i]<=pivot :
            if i!=split :
                # if split==0:
                #     swap=0
                # else:
                #     swap=split
                temp=A[i]
                A[i]=A[split]
                A[split]=temp
            split=split+1
        print(A,"split:",split,"i",i)
    return split-1


