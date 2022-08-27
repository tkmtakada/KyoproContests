

def solve(N):
    k = 998244353
    r = N % k
    print(r)
    return 0



def input_args():
    N = int(input())
    return [N]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)