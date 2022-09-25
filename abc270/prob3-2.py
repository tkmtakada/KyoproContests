from collections import deque

def solve(N, X, Y, adj):
    # bfsだと、単純バスは出しづらい
    # dfsで
    used = [0 for _ in range(N)]
    used[X-1] = 1
    deq = deque()
    deq.append(X-1)
    dfs(adj, deq, Y, used)
    return 0

def dfs(adj, path, Y, used):
    # conditions
    # 自己ループは避けたい
    # そういう時は、一回一回戻せばいいんだっけ？　usedに印をつけて
    
    cands = adj[path[-1]]
    for elt in cands:
        if elt == Y-1:
            ans = path + [elt]
            print(*[elt+1 for elt in ans])
            return

        if used[elt] == 0:
            used[elt] = 1
            dfs(adj, path+[elt], Y, used)
            used[elt] = 0

def input_args():
    return []

def test():
    N, X, Y = map(int, input().split())
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    return [N, X, Y, adj]


if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)