"""
Problem:
------------
In this challenge, you will be given 2 integers, n and m. There are n words,
which might repeat, in word group A. There are m words belonging to word
group B. For each m words, check whether the word has appeared in group A or
not. Print the indices of each occurrence of m in group A. If it does not
appear, print -1.

Input Format:
-------------
The first line contains integers, n and m separated by a space.
The next n lines contains the words belonging to group A.
The next m lines contains the words belonging to group B.

Output Format:
-------------
Output m lines. The ith line should contain the 1-indexed positions of the
occurrences of the ith word separated by spaces.
"""

from collections import defaultdict

ui = input().split()
n = int(ui[0])
m = int(ui[1])

nDict = defaultdict(list)
mList = []
for i in range(n):
    nDict[input()].append(i+1)
for i in range(m):
    mList.append(input())
for i in mList:
    if i in nDict.keys():
        t = list(map(str,nDict[i]))
        print(' '.join(t))
    else:
        print('-1')
