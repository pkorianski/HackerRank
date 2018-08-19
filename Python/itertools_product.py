"""
Problem:
----------_
You are given a two lists A and B. Your task is to compute their
cartesian product AxB.

Input Format:
-------------
The first line contains the space separated elements of list A.
The second line contains the space separated elements of list B.

Both lists have no duplicate integer elements.

Output Format:
-------------
Output the space separated tuples of the cartesian product.
"""

from itertools import product
t1 = tuple(map(int,input().split()))
t2 = tuple(map(int,input().split()))
result = ""
l = list(product(t1,t2))
for i,t in enumerate(l):
    if i != len(l)-1:
        result += str(t) + ' '
    else:
        result += str(t)
print(result)
