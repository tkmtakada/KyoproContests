

def mysolve(N, L, R, A):
    # LEFT 
    
    # get cumsum
    cumsum_l = [0 for _ in range(N+1)]
    sum_l = 0
    for i in range(len(A)):
        cumsum_l[i+1] = cumsum_l[i] + A[i]
    cumsum_l = cumsum_l[1:]
    
    # get the optimal x
    idx = -1
    max_diff = -float('inf')
    for i in range(len(A)):
        cur_diff = cumsum_l[i] - L * (i+1)
        if cur_diff > 0 and cur_diff > max_diff:
            max_diff = cur_diff
            idx = i
    # print("LEFT", idx)
    
    if idx == -1:
        pass  # do nothing
    else:
        for i in range(idx+1):
            A[i] = L
    # print("LEFT OPERATION IS DONE: ", A)

    # RIGHT


    # get cumsum
    cumsum_r = [0 for _ in range(N+1)]
    sum_r = 0
    for i in range(len(A)):
        cumsum_r[i+1] = cumsum_r[i] + A[-(i+1)]
    cumsum_r = cumsum_r[1:]
    
    # get the optimal x
    idx = -1
    max_diff = -float('inf')
    for i in range(len(A)):        
        cur_diff = cumsum_r[i] - R * (i+1)
        if cur_diff > 0 and cur_diff > max_diff:
            max_diff = cur_diff
            idx = i
    # print("RIGHT", idx)
    
    if idx == -1:
        pass  # do nothing
    else:
        for i in range(idx+1):
            A[-(i+1)] = R
    # print("RIHGT OPERATION IS DONE: ", A)
    
    
    print(sum(A))

    return 0

def solve(N, L, R, A):
    f = [0 for _ in range(N+1)]
    for i in range(N):
        f[i+1] = min(f[i] + A[i], L * (i+1))

    g = [0 for _ in range(N+1)]
    for j in range(N):
        g[j+1] = min(g[j] + A[-(j+1)] , R * (j+1))

    h = [0 for _ in range(N+1)]
    for i in range(len(f)):
        h[i] = f[i] + g[N-i]
    
    print(min(h))

def input_args():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    return [N, L, R, A]

def test():
    N, L, R = 5,  4, 3
    A = [5, 5, 0, 6, 3]

    return [N, L, R, A]

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)