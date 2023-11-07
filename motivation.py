#https://www.codechef.com/practice/LP1TO201/problems/IMDB

# cook your dish here
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n,x=map(int, input().split(" "))
    l=[]
    for i in range(n):
        si,ri=map(int,input().split(" "))
        if si<=x:
            l.append(ri)
    print(max(l))