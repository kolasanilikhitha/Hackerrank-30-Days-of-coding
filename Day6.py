'''
Task
Given a string, S, of length  that is indexed from 0 to N-1 , print its even-indexed and odd-indexed characters as  space-separated strings on a single line (see the Sample below for more detail).
Note: 0 is considered to be an even index.
Example
s=abcdef
Print abc def

Input Format

The first line contains an integer, T (the number of test cases).
Each line i of the T subsequent lines contain a string,S .
Constraints
1<=T<=20
2<=length of s<=10000
Output Format
For each String sj  (where0<=j<=T-1 ), print sj's even-indexed characters, followed by a space, followed by sj's odd-indexed characters.
Sample Input
2
Hacker
Rank
Sample Output
Hce akr
Rn ak
'''
code:
# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input())
k=[]
for i in range(0, T):
    k.append(input())
for j in range(0, T):
    e=""
    o=""
    for i in range(0, len(k[j])):
        if (i% 2==0):
            e+=k[j][i]
        else:
            o+=k[j][i]
    print(e +" "+o)
