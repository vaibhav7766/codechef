#https://www.codechef.com/practice/LP1TO201/problems/WEIGHTBL

# cook your dish here
import sys
input = sys.stdin.readline

def weight(w1, w2, x1, x2, m):
    min_wt=x1*m
    max_wt=x2*m
    a=abs(w2-w1)
    if a>=min_wt and a<=max_wt:
        return 1
    else:
        return 0
for _ in range(int(input())):
    w1,w2,x1,x2,m=map(int, input().split())
    print(weight(w1,w2,x1,x2,m))