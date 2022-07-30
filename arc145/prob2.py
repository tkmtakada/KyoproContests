

def solve(N, A, B):
    AgtB = (A >= B)
    if A >= B:        
        # count = 0
        # for n in range(1, N+1):
        #     print(n)
        #     if n < A:
        #         pass  # Aの負け
        #     elif (n % A) < B:
        #         count += 1
        r = N // A
        q = N % A
        if r >= 1:
            count = (r-1) * B + 1 + min(q, B-1)
        else:
            count = 0
        print(count)

    else:
        # count = 0
        # for n in range(1, N+1):
        #     if n < A:
        #         pass  # 取れないから、Aの負け
        #     else:  # 最大限取った時のあまりはBは絶対とれない
        #         count += 1
        if N >= A:
            count = N - A + 1
        else:
            count = 0
        print(count)

    return 0



def input_args():
    N, A, B = map(int, input().split())
    return [N, A, B]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)