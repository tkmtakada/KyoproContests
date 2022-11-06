

def solve(N, M, adj):
    for i in range(1, N+1):
        if i in adj:
            lst = adj[i]
            print(len(lst), *sorted(lst))
        else:
            print(0)
    return 0



def input_args():
    N, M = map(int, input().split())
    adj = {}
    for _ in range(M):
        a, b = map(int, input().split())
        if a in adj:
            adj[a].append(b)
        else:
            adj[a] = [b]
        # ---
        if b in adj:
            adj[b].append(a)
        else:
            adj[b] = [a]
    return [N, M, adj]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)