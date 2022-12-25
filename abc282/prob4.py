

def solve(N, M, adj):
    
    return 0



def input_args():
    N, M = map(int, input().split())
    adj = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    return [N, M, adj]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)