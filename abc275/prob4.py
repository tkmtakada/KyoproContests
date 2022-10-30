

def solve(N):
    dp = [1] * (N+1)
    for i in range(1, N+1):
        dp[i] = dp[(i // 2)] + dp[(i // 3)]
    print(dp[N])
    print(dp)
    return 0



def input_args():
    N = int(input())
    return [N]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)