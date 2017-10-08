A=[1,2,3,4,5]
print(A)

for i in range(0,len(A)):
    for j in range(i,i+8):
        if j<len(A):
            print(A[j])