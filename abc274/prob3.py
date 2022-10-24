

def solve(N, A):
    dp = [0 for _ in range(2*N+2)] # 0 ~ 2N+1 の計2N+2
    for idx in range(1, N+1):        
        dp[2*idx] = dp[A[idx-1]] + 1
        dp[2*idx+1] = dp[A[idx-1]] + 1
        
    # ans
    for i in range(2*N+1):
        print(dp[i+1])
    return 0



def input_args():
    N = int(input())
    A = list(map(int, input().split()))
    return [N, A]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)