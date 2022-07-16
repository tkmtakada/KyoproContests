

def solve(N, a, b, A):
    A.sort()
    while True:
        # A.sort()
        # print("A: ", A)
        minVal = A[0]
        secondMinVal = A[1]
        maxVal = A[-1]
        if minVal + a <= maxVal - b:
            # minValとmaxValの位置更新
            A[0] +=  a 
            # binary searchで
            A[-1] -= b
            A.sort()
        elif secondMinVal <= maxVal - b:
            A[0] += a
            A[-1] -= b
            A.sort()
        else:
            print(A[0])
            break



def input_args():
    N, a, b = map(int, input().split())
    A = list(map(int, input().split()))
    return N, a, b, A

def test():
    return 

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)