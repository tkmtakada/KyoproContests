

def solve(N, A):
    count_same = 0    
    count_swap = 0
    for i, a in enumerate(A):
        idx = i + 1
        if idx == a:
            count_same += 1
        elif A[a-1] == idx:
            count_swap += 1
    ans = (count_same * (count_same - 1) + count_swap) // 2 
    print(ans)


def input_args():
    N = int(input())
    A = list(map(int, input().split()))
    return [N, A]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)