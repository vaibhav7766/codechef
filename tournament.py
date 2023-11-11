#https://www.codechef.com/ZCOPRAC/problems/ZCO13001?tab=statement

# cook your dish here
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

ans=0

arr.sort()
for i in range(n):
    ans+=arr[i]*i
    ans-=arr[i]*(n-(i+1))

print(ans)