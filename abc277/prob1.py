

def solve(N, X, P):
    print(P.index(X)+1)
    return 0



def input_args():
    N, X = map(int, input().split())
    P = list(map(int, input().split()))
    return [N, X, P]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)