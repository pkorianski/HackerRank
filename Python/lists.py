"""
Problem:
------------
Consider a list (list = []). You can perform the following commands:

1) insert i e: Insert integer e at position i.
2) print: Print the list.
3) remove e: Delete the first occurrence of integer e.
4) append e: Insert integer  at the end of the list.
5) sort: Sort the list.
6) pop: Pop the last element from the list.
7) reverse: Reverse the list.

Initialize your list and read in the value of  followed by lines of commands
where each command will be of the types listed above. Iterate through each
command in order and perform the corresponding operation on your list.

Input Format:
-------------
The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

Output Format:
-------------
For each command of type print, print the list on a new line.
"""

if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        x = input()
        x = x.split()
        if x[0] == 'print':
            print(l)
        elif len(x) == 1:
            eval('l.'+x[0]+'()')
        elif len(x) == 2:
            eval('l.'+x[0]+'(' + x[1] +')')
        else:
            eval('l.'+x[0]+'('+ x[1] + ',' + x[2] +')')
