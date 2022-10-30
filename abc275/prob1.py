

def solve(N, lst):
    idx = lst.index(max(lst))
    print(idx+1)
    return 0



def input_args():
    N = int(input())
    lst = list(map(int, input().split()))
    return [N, lst]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)