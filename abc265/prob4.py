

def solve(N, P, Q, R, A):
    cumsum = [0]
    for a in A:
        cumsum.append(cumsum[-1] + a)

    # subsum がPになるところを探す
    for ... :
        ...
        #" そこ以降で subsum がQを探す
        for ... in ...:

            # find part whose subsum equals to R
            for  ... in ...:

    return 0



def input_args():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input()))
    return [N, P, Q, R, A]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)