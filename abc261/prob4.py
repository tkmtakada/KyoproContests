

def solve(N, M, X, Bonus):
    def getBonus(i):
        if i in Bonus:
            return Bonus[i]
        else:
            return 0
    dp = [[0 for _ in range(N)] for _ in range(N)]
    for cnt in range(N):
        dp[cnt][N-1] = X[N-1] + getBonus(cnt+1)


    # DPを実行
    for pos in reversed(range(N-1)):
        for cnt in range(pos+1):
            dp[cnt][pos] = max(dp[cnt+1][pos+1]+X[pos] + getBonus(cnt+1),  # 表
                                dp[0][pos+1])  # 裏
    print(dp[0][0])

def input_args():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    Bonus = {}
    for _ in range(M):
        counter, point = map(int, input().split())         
        Bonus[counter] = point
    return [N, M, X, Bonus]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)