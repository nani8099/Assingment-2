# Write a Python program to get a list,sorted in increasing order by the last element in each element in eachh tuple from a given list of non_empty tuples.

# Sample List : [(2,5),(1,2),(4,4),(2,3),(2,1)]

# Expected Result : [(2,1),(1,2),(2,3),(4,4),(2,5)]


def last(n):
    return n[-1]
def sort(a):
    return sorted(a,key=last)
a = [(2,5),(1,2),(4,4,),(2,3),(2,1)]
print(sort(a))
   


#    OUTPUT:

#    [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]




    





