######first 3 sort#################
# import Insertionsort
# import mergesort
#
#
# # vec1=Insertionsort.insertion(myfun.random_int_list(1, 100, 10))
# # vec2=Insertionsort.insertion(myfun.random_int_list(1, 100, 10))
# vec=myfun.random_int_list(1, 100, 50)
# vec1=[1,7,4,3,5,8,6,2]
# #vec=[6,5,3,1,8,7,2,4]
# #vec=[3,2,1]
# # vec=vec1+vec2
# # print(vec1,vec2)
# print(vec)
# mergesort.mergesort(vec1,0,len(vec1)-1)
# print (vec1)

####binary search #########################
# import binarysearch
# import mergesort
# vec=myfun.random_int_list(1, 10, 10)
# mergesort.mergesort(vec,0,len(vec)-1)
# #vec=[1,2,3,4,4,6,8,9,10,10]
# x=5
# print(vec,x)
# print(binarysearch.binarysearch(x,vec,0,9))

#####quick sort###############################
# import quicksort
# vec=myfun.random_int_list(0, 100, 20)
# print(vec)
# #print(quicksort.Partition(vec,1,9))
# quicksort.quicksort(vec,0,len(vec)-1)
# print(vec)



#####pairdist################################




####DFS###############################
import numpy
# a, b, c, d, e, f, g, h = range(8)
# N = [
#     [b, c, d, e, f],  # a
#     [c, e],  # b
#     [d],  # c
#     [e],  # d
#     [f],  # e
#     [c, g, h],  # f
#     [f, h],  # g
#     [f, g]  # h
#     ]
# # print(type(N))
# print(numpy.size(N))
# print(g in N[a])


# graph = { "a" : ["c"],
#           "b" : ["c", "e"],
#           "c" : ["a", "b", "d", "e"],
#           "d" : ["c"],
#           "e" : ["c", "b"],
#           "f" : []
#         }
# #print(graph)
# print(graph.keys())

a=[1,2,3]
b=[3,4,5]
print([a]+[b])








