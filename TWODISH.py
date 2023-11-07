#https://www.codechef.com/practice/LP1TO201/problems/TWODISH

# cook your dish here
import sys
input = sys.stdin.readline

def can(n,a,b,c):
    count1=min(a,b)
    b-=a
    count2=min(b,c)
    if count1+count2>=n:
        return "YES"
    else:
        return "NO"
    

for _ in range(int(input())):
    n,a,b,c=map(int,input().split(" "))
    print(can(n,a,b,c))