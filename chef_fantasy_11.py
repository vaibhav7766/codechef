#https://www.codechef.com/problems/FIZZBUZZ2303

# cook your dish here
import sys
from math import perm
input = sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    print(perm(n,2))