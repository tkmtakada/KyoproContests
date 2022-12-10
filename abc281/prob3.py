

def solve(N, T, A):
    total = 0
    cumsum = []  # i番目の値は、i曲目が終わる時間
    for a in A:
        total += a            
        cumsum.append(total)
    
    # finish making cumsum
    total_length = total

    # まず何周目なのかを突き止める
    r = T // total_length
    q = T % total_length

    # q分目が、何曲目かを二分探索で探索？？
    # まずは例外処理、範囲内にない可能性もあるので。
    if q <= cumsum[0]:
        print("{} {}".format(1, q))
        return
    # 普通に二分探索できる時
    s, e = 0, N-1
    while s+1 < e:
        m = (s + e) // 2
        if cumsum[m] <= q:
            s = m 
        else:  # cumsum[m] > T
            e = m
    print("{} {}".format(e+1, q-cumsum[s]))


    return 0



def input_args():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    return [N, T, A]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)