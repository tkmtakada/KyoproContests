

def solve(N, M, X):
    # 普通に総当たり
    for i in range(N):
        for j in range(i+1, N):
            attendedSame = False
            for k in range(M):
                if X[k][i] == 1 and X[k][j] == 1:
                    attendedSame = True
                    break
            if not attendedSame:
                print('No')
                return
    print('Yes')    
    return 0



def input_args():
    N, M = map(int, input().split())
    X = [[0 for _ in range(N)] for _ in range(M)]
    for m in range(M):
        k_x = list(map(int, input().split()))
        for idx in k_x[1:]:
            X[m][idx-1] = 1
        # X.append(k_x[1:])
    return [N, M, X]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)