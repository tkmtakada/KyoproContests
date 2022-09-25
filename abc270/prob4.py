

def solve(N, K, A):
    r = N // A[-1]
    tp = 0
    ap = 0
    if r % 2 == 0:  # 残りも高橋君スタート
        tp += A[-1] * (r//2)
        ap = tp
        N = N % A[-1]
        _tp, _ap = run(tp, ap, N, A)
        print(_tp)
    else:  # start from Aoki
        ap = A[-1] * (r//2)
        tp = ap + A[-1]
        N = N % A[-1]
        _ap, _tp = run(ap, tp, N, A)
        print(_tp)
    
    return 0

def run(tp, ap, N, A):
    while N > 0:
        # takahashi
        for a in reversed(A):
            if a <= N:
                tp += a
                N -= a
                break
        
        # aoki
        for a in reversed(A):
            if a <= N:
                ap += a 
                N -= a
                break
    return tp, ap
        

def solve2(N, K, A):
    # https://atcoder.jp/contests/abc270/editorial/4850 
    dp = [0 for _ in range(N+1)]
    dp[1] = 1
    for n in range(2, N+1):
        cands = [a for a in A if a <= n]
        maxv = 0
        for a in cands:
            if a <= n:
                maxv = max(a + (n-a) - dp[n-a], maxv)
        dp[n] = maxv
    print(dp[N])


    return 0        

def input_args():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    return [N, K, A]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    # solve(*args)
    solve2(*args)