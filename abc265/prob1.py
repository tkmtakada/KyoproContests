

def solve(X, Y, N):
    if Y < 3 * X:
        r = N // 3
        q = N % 3
        print(r * Y + q * X)
    else:
        print(N * X)
    



def input_args():
    X, Y, N = map(int, input().split())    
    return [X, Y, N]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)