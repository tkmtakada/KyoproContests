
import numpy as np
# from pdb import set_trace as db

def mySolve(N, X,Y, Z, A, B):
    idList = np.array(list(range(N)))
    A = np.array(A)
    B = np.array(B)
    # db()
    # lst = [idList, A, B]
    # arr = np.array(lst)
    ans = []

    # 数学とる
    idx = np.argsort(-A)
    sortedId = idList[idx]
    sortedA = A[idx]
    sortedB = B[idx]
    ans.extend(sortedId[:X].tolist())

    idList = sortedId[X:]
    A = sortedA[X:]
    B = sortedB[X:]
    idList, A, B = sortAll(idList, A, B)
    
    # 英語とる
    idx = np.argsort(-B)
    sortedId = idList[idx]
    sortedA = A[idx]
    sortedB = B[idx]
    ans.extend(sortedId[:Y].tolist())

    idList = sortedId[Y:]
    A = sortedA[Y:]
    B = sortedB[Y:]
    idList, A, B = sortAll(idList, A, B)


    # 総合点で選ぶ
    C = np.array([a + b for a, b in zip(A,B)])
    idx = np.argsort(-C)
    sortedId = idList[idx]

    ans.extend(sortedId[:Z].tolist())
    ans.sort()  # sort
    for num in ans:
        print(num + 1)

def solve(N, X, Y, Z, A, B):
    passed = [False for _ in range(N)]
    # 数学
    C = [(100 - A[i]) * 1000 + i for i in range(N)]
    C.sort()
    for i in range(X):
        passed[C[i]%1000] = True

    # 英語
    C = [(100 - B[i]) * 1000 + i for i in range(N) if passed[i] == False]
    C.sort()
    for i in range(Y):
        curIdx = C[i] % 1000
        passed[curIdx] = True

    # 総合
    C = [(200 - A[i] - B[i]) * 1000 + i for i in range(N) if passed[i] == False]
    C.sort()
    for i in range(Z):
        curIdx = C[i] % 1000
        passed[curIdx] = True
    
    for i in range(N):
        if passed[i] == True:
            print(i+1)
    return 


def sortAll(idList, A, B):
    # 全てnumpyの想定
    idx = np.argsort(idList)
    return idList[idx], A[idx], B[idx]

def input_args():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    return [N, X,Y, Z, A, B]

def test():
    print("!! WARING!! THIS IS TEST!!")
    N, X, Y, Z = 6, 1, 0, 2
    A = [80, 60, 80, 60, 70, 70]
    B = [40, 20, 50, 90, 90, 80]
    return [N, X, Y, Z, A, B]

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)