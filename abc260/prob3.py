def convertFromRed(N, X):

    R = [0 for _ in range(N+1)]  # レベル0も含めている
    B = [X for _ in range(N+1)]
    R[1] = 1
    B[0] = B[1] = 0
    
    return R, B

def convertFromBlue(N, Y):
    if N == 1:
        return 
    B = [0 for _ in range(N+1)]  # レベル0も含めている
    R = [0 for _ in range(N+1)]
    B[1] = Y**(N-1)
    for i in range(1, N):
        R[i] = Y**(N-1-i)
    return R, B
def mySolve(N, X, Y):
    R, B = convertFromRed(N, X)
    for i in range(1, len(B)):
        b = B[i]
        R, B = convertFromBlue(i, Y)

def solve(N, X, Y):
    R = [0 for _ in range(N+1)]
    B = [0 for _ in range(N+1)]
    B[1] = 1
    for i in range(2, N+1):
        B[i] = R[i-1] + Y * B[i-1]
        R[i] = R[i-1] + X * B[i]
    
    print(R[N])
    return



def input_args():
    N, X, Y = map(int, input().split())
    return [N, X, Y]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)