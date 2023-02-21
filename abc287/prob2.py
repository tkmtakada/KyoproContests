

def solve(N, M, S, T):
    counter = 0
    for s in S:
        if s[-3:] in T:
            counter += 1
    print(counter)
    return 0



def input_args():
    N, M = map(int, input().split() )    
    S = []
    for _ in range(N):
        S.append(input())
    T = {}
    for _ in range(M):
        t = input()
        T[t] = True

    return [N, M, S, T]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)