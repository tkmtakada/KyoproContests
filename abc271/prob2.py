

def solve(N, Q, seqList, queryList):
    for s, t in queryList:
        print(seqList[s-1][t-1])
    return 0



def input_args():
    N, Q = map(int, input().split())
    seqList = []
    for _ in range(N):
        s = list(map(int, input().split()))
        seqList.append(s[1:])
    queryList = []
    for _ in range(Q):
        s,t = map(int, input().split())
        queryList.append([s,t])
    return [N, Q, seqList, queryList]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)