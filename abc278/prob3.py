

def solve(N, Q, queries):
    followers = {}
    for t, a, b in queries:
        if t == 1:
            if a in followers:
                followers[a].add(b)
            else:
                followers[a] = set([b])
        elif t == 2:
            if a in followers:
                followers[a].discard(b)
            else:
                pass 
        elif t == 3:

            if (a in followers) and (b in followers) and \
                (b in followers[a]) and (a in followers[b]):
                print('Yes')
            else:
                print('No')
    return 0



def input_args():
    N, Q = map(int, input().split())
    queries = []
    for _ in range(Q):
        t, a, b = map(int, input().split())
        queries.append([t,a,b])
    return [N, Q, queries]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)