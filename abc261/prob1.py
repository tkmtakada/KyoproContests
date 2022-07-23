

def solve(l1, r1, l2, r2):        
    if l2 <= l1:
        if r2 < l1:
            ans = 0
        else:
            ans = min(r1, r2) - l1
    elif l2 <= r1:
        ans = min(r1, r2) - l2
    elif r1 < l2:
        ans = 0
    print(ans)
    return 0


def input_args():
    l1, r1, l2, r2 = map(int, input().split())
    return [l1, r1, l2, r2]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)