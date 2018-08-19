"""
Problem:
------------
Given the names and grades for each student in a Physics class of N students,
store them in a nested list and print the name(s) of any student(s) having the
second lowest grade.

Input Format:
-------------
The first line contains an integer,N,the number of students. The 2N subsequent
lines describe each student over 2 lines; the first line contains a student's
name, and the second line contains their grade.

Output Format:
--------------
Print the name(s) of any student(s) having the second lowest grade in Physics;
if there are multiple students, order their names alphabetically and print each
one on a new line.

Explanation 0:
--------------
There are  students in this class whose names and grades are assembled to
build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2],
                   ['Akriti', 41], ['Harsh', 39]]

The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21
belongs to both Harry and Berry, so we order their names alphabetically and
print each name on a new line.

"""

if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([score,name])
    l2 = list(set([i for i,j in l]))
    l2.sort()
    out = [j for i,j in l if i == l2[1]]
    out.sort()
    for name in out:
        print(name)
