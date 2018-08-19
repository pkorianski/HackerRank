"""
Problem:
-----------
Raghu is a shoe shop owner. His shop has  number of shoes. He has a list
containing the size of each shoe he has in his shop. There are N number of
customers who are willing to pay x amount of money only if they get the shoe
of their desired size.

Your task is to compute how much money Raghu earned.

Input Format:
------------
The first line contains X, the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains N, the number of customers.
The next N lines contain the space separated values of the shoe size desired by
the customer and x, the price of the shoe.

Output Format:
--------------
Print the amount of money earned by Raghu.
"""

x = int(input())
l = input().split()
n = int(input())
c = 0
for i in range(n):
    t = input().split()
    if t[0] in l:
        c += int(int(t[1]))
        l.remove(t[0])
print(c)
    
