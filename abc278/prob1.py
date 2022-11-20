

def solve(N, K, A):
    ans = A[K:] + ([0] * min(K, N))
    print(*ans[:N])
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
    solve(*args)