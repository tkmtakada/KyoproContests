
 
def solve(N, M):
    # dfs    
    # ans = []
    path = []
    cand = list(range(1, M+1))
    dfs(path, cand, 0, N)
    # print(ans)


def dfs(path, cand, length, N):
    # ending conditions
    if length == N:
        print(*path)
        # ans.append(path)
        return 
    if len(cand) == 0:
        return

    for idx, val in enumerate(cand):
        dfs(path+[val], cand[idx+1:], length+1, N)



def input_args():
    N, M = map(int, input().split())
    return [N, M]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)