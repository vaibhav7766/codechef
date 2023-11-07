#https://www.codechef.com/practice/LP1TO201/problems/PROGLANG

# cook your dish here
import sys
input = sys.stdin.readline

def compatible(a,b,a1,b1,a2,b2):
    count=0
    if (a,b)==(a1,b1) or (a,b)==(b1,a1):
        count=1
    if (a,b)==(a2,b2) or (a,b)==(b2,a2):
        count=2
    return count

for _ in range(int(input())):
    a,b,a1,b1,a2,b2=map(int, input().split(' '))
    print(compatible(a,b,a1,b1,a2,b2))