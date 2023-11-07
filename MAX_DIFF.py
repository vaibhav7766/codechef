#https://www.codechef.com/practice/LP1TO201/problems/MAX_DIFF

# cook your dish here
import sys
input = sys.stdin.readline

def max_abs_diff(n,s):
    if s<n:
        mini=0
        maxi=s
    else:
        maxi=n
        mini=s-n
    return abs(maxi-mini)

for _ in range(int(input())):
    n,s=map(int, input().split(" "))
    print(max_abs_diff(n,s))