

def solve(N, M, T, A, bonus):
    
    for i, a_i in enumerate(A):
        # 部屋 i にたどりつきました
        if i+1 in bonus:
            T += bonus[i+1]
        
        # a_iを消費してnext roomに行きます
        T -= a_i
        if T <= 0:
            print("No")
            return 0
    print("Yes")
    return 0


def input_args():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    bonus = {}
    for _ in range(M):
        x, y = map(int, input().split())
        bonus[x] = y
        
    return [N, M, T, A, bonus]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)