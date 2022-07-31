

def solve(N, M, edges, mp):
    ans = 0
    for a in range(1, N-1):
        for b in range(a, N):
            for c in range(b, N+1):
                # 判定
                if b in mp[a] and c in mp[b] and a in mp[c]:
                    ans += 1
    print(ans)
    



def input_args():
    N, M = map(int, input().split())
    edges = []
    mp = {}
    for _ in range(M):
        u, v = map(int, input().split())
        if u in mp:
            mp[u].append(v)
        else:
            mp[u] = [v]

        if v in mp:
            mp[v].append(u)
        else:
            mp[v] = [u]
    return [N, M, edges, mp]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)