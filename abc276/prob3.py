


def solve(N, P):
    cur = N - 2
    while cur >= 0:
        # check if there is smaller element than P[cur]    
        validSmallerNum = -float('inf')
        validSmallerNumIdx = None
        for i in range(cur+1, N):
            elt = P[i]    
            if elt < P[cur]:
                validSmallerNum = max(elt, validSmallerNum)
                validSmallerNumIdx = i
        # if validSmallerNum exist, just do swapping and do sorting again
        if validSmallerNumIdx is not None:
            P[cur], P[validSmallerNumIdx] = P[validSmallerNumIdx], P[cur]  # swap
            P[cur+1:] = sorted(P[cur+1:], reverse=True)
            print(*P)
            return 
        else:
            cur -= 1
    
    return 0



def input_args():
    N = int(input())
    P = list(map(int, input().split()))
    return [N, P]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)