

def solve(N, M, A):
    cur_max = -float('inf')
    total = 0
    sum_m = 0
    for i in range(M):
        total += (i+1) * A[i]
        sum_m += A[i]
    
    cur_max = total
    for i in range(M, N):
        total = total - sum_m + A[i] * M
        sum_m = sum_m + A[i] - A[i-M]

        cur_max = max(cur_max, total)
    print(cur_max)

    return 0



def input_args():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    return [N, M, A]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)