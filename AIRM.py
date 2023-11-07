#https://www.codechef.com/problems/AIRM?tab=statement

# cook your dish here
import sys
from collections import Counter
input = sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int, input().split(' ')))
    dep=list(map(int, input().split(' ')))
    l=Counter()
    for i,j in zip(arr,dep):
        l[i]+=1
        l[j]+=1
    print(sorted(l.values())[-1])