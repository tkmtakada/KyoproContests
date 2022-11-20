
"""
全ての値を、base（全要素で共通している部分、Type1がきた時はこれ）と、
 各要素の、ベースからの差分で、管理すれば行けたらしい
"""
def solve(N, A, Q, queries):
    # 先に追うべき場所を調べておく必要あり
    targets = []
    for q in queries:
        if q[0] == 3:
            targets.append(q[1])
    
    for q in queries:
        if q[0] == 1:            
            for idx in targets:
                A[idx-1] = q[1]
        elif q[0] == 2:
            A[q[1]-1] += q[2]
        elif q[0] == 3:
            print(A[q[1]-1])
    
    return 0



def input_args():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = []
    for _ in range(Q):
        q = list(map(int, input().split()))
        queries.append(q)
    return [N, A, Q, queries]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)