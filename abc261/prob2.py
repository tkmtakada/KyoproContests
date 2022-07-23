

def solve(N, A):
    for i in range(1, N):
        for j in range(i):
            if (A[i][j], A[j][i]) not in [('W', 'L'), ('L', 'W'), ('D', 'D')]:
                print("incorrect")
                return 
    print("correct")
    return 0


def input_args():
    N = int(input())
    A = []
    for _ in range(N):
        s = input()
        A.append(list(s))
    return [N, A]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)