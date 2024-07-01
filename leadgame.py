# https://www.codechef.com/practice/course/zco-inoi-problems/IARCSJUD/problems/LEADGAME

n = int(input())

player1_cumulative = 0
player2_cumulative = 0

max_lead = 0
leader = 0

for _ in range(n):
    a, b = map(int, input().split())
    player1_cumulative += a
    player2_cumulative += b

    current_lead = player1_cumulative - player2_cumulative

    if abs(current_lead) > max_lead:
        max_lead = abs(current_lead)
        leader = 1 if current_lead > 0 else 2

print(leader, max_lead)
