"""
RE

アルゴリズムはあってるはず、模範解答ともほぼ一致（Dequeをつかってたが）
"""

def solve(N, X, Y, adj):
    # bfsだと、単純バスは出しづらい
    # dfsで
    used = [0 for _ in range(N)]
    used[X-1] = 1
    dfs(adj, [X-1], Y, used)
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
            used[elt] = 0  # 模範解答では、ここがないかも？確かにdequeを使って分岐点まで戻れるなら、いらないかも？



def input_args():
    N, X, Y = map(int, input().split())
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    return [N, X, Y, adj]

def test():
    """
    6 1 5
    1 2
    1 3
    2 3
    3 6
    3 4
    """
    return []



if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)