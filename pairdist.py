import math


def distance(A,B):
    return math.sqrt((A[0]-B[0])^2+(A[1]+B[1])^2)

def pairdist(A):
    if len(A)<2:
        return 0
    elif len(A)==2:
        return distance(A[0],A[1])
    else:
        A.sort()
        m = round(len(A)/2)
        L = A[:m]
        R = A[m:]
        dL = pairdist(L)
        dR = pairdist(R)
        d = min(dL,dR)

        k=0
        B=[]
        for i in range(0,len(A)):
            if A[i][0]-m>d or m-A[i][0]>d:
                B[k]=A[i]
                k=k+1
        B.sort(key=lambda x: x[1])
        for i in range(0,len(B)):
            for j in range(i+1,i+8):
                if j<len(B):
                    dtemp=distance(B[i],B[j])
                    if dtemp<d:
                        d=dtemp
        return (d)



