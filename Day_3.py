'''
Task:
Given an integer, , perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5 , print Not Weird
If  is even and in the inclusive range of 6 to 20 , print Weird
If  is even and greater than 20, print Not Weird
Complete the stub code provided in your editor to print whether or not n  is weird.

Input Format:
A single line containing a positive integer, .
Constraints
1<=n<=100
Output Format:

Print Weird if the number is weird; otherwise, print Not Weird.

Sample Input 0
3
Sample Output 0
Weird
Sample Input 1
24
Sample Output 1
Not Weird
'''
#code:
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    if (((N%2)==0) and ((2<=N<=5) or (N>20))):
        print("Not Weird")
    elif((N%2==0) and (6<=N<=20)):
        print("Weird")
    elif((N%2)!=0):
        print("Weird")
        
