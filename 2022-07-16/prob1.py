

def solve(N):
    # Mをもとめる
    if N < 4:
        M = 2 * N
        print(M)
    else:
        num4 = N // 4
        rest = N % (4 * num4)
        M = 8 * num4 + 2 * rest
        print(M)
    digitsM = num4 + 1 if rest != 0 else num4

    # x を求める
    flag = True
    numDigits = 1
    while numDigits <= digitsM:
        if N < numDigits * 9:
            ...
            numDigits += 1  # Mに一致するものがないため
        else:  # 桁が足りない
            numDigits += 1

    



def input_args():
    N = int(input())
    return [N]

def test():
    N = 6
    return [N] 

if __name__=="__main__":
    # args = input_args()
    args = test()
    solve(*args)