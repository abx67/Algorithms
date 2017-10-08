####Partition##################
def Partition(A,left,right):
    if left>=right:
        return right
    else:
        split=left
        pivot=A[right]
        print("pivot",pivot)
        for i in range(left,right+1):
            print("i",i)
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
            #print(A,"split:",split,"i",i)
        return split-1

#####quicksort#######
def quicksort(A,left,right):
    if right!=left:
        split=Partition(A,left,right)
        print("split:",split,"left",left,"right",right)
        print("A",A)
        if split >= left + 1:
            quicksort(A,left,split-1)
        if split <= right - 1:
            quicksort(A,split+1,right)
    else:
        return

