

def solve(N, A):
    # 例外処理
    if len(A) == 2:
        if (A[0]%2 + A[1]%2) == 1:
            print(-1)
            return

    inf = float('inf')
    even_max = [-inf, -inf]
    odd_max = [-inf, -inf]
    for elt in A:
        if elt % 2 == 0:  # even
            even_max = updateTop2(even_max, elt)
        else:
            odd_max = updateTop2(odd_max, elt)
    
    print(max(sum(even_max), sum(odd_max)))
    return 0

def updateTop2(curTop2, cand):
    if cand > curTop2[0]:
        return [cand, curTop2[0]]
    elif cand > curTop2[1]:
        return [curTop2[0], cand]
    else:
        return curTop2



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