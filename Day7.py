'''
Task
Given an array, A, of Nintegers, print A's elements in reverse order as a single line of space-separated numbers.
Example
A=[1,2,3,4]
Print 4 3 2 1. Each integer is separated by one space.
Input Format
The first line contains an integer,N  (the size of our array).
The second line contains N space-separated integers that describe array A 's elements.

Constraints

Constraints
1<=N<=1000
1<=A[i]<=10000

, where  is the  integer in the array.
Output Format

Print the elements of array A in reverse order as a single line of space-separated numbers.

Sample Input

4
1 4 3 2
Sample Output

2 3 4 1
'''
code:
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    k=len(arr)-1
    for i in range(k, -1, -1):
        print(str(arr[i]),end=" ")
