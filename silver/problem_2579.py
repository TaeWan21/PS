N = int(input())
dp = []
stairs = [0] * 300 

for i in range(N):
    stairs[i] = int(input())

dp = [0] * 300
dp[0] = stairs[0]
dp[1] = max(stairs[0]+ stairs[1], stairs[1])
dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

# i-3, i-1, i /  i-2, i
for i in range(3, N):
    dp[i] = max(dp[i - 3] + stairs[i -1] + stairs[i], dp[i -2] + stairs[i])

print(dp[N-1])