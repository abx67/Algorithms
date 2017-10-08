def binarysearch(x,A,left,right):
    mid=left+round((right-left)/2)
    if(x==A[mid]):
        return mid
    elif(right==left):
        return
    elif(x>A[mid]):
        left=mid+1
    else:
        right=mid
    return (binarysearch(x, A, left, right))