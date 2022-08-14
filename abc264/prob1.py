

def solve(L, R):
    s = "atcoder"
    print(s[L-1:R])



def input_args():
    L, R = map(int, input().split())
    return [L, R]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)