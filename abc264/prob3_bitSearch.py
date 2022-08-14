

def solve(h1, w1, A, h2, w2, B):
    for i in range(2 ** h1):
        for j in range(2 ** w1):
            # i, j はそれぞれbitと見做している            
            hvec = []
            wvec = []
            for k in range(1, h1+1):
                if (i & (1 << (k-1) )) == 0:  # シンプルに、bit表記した時に、ｋ番目が1かどうかを調べている
                    hvec.append(k-1)
            for k in range(1, w1+1):
                if (j & (1 << (k-1))) == 0:
                    wvec.append(k-1)
            
            if len(hvec) != h2 or len(wvec) != w2:
                pass
            else:  # 形が等しい
                isSame = True
                for k in range(h2):
                    for l in range(w2):
                        r_a = hvec[k]
                        c_a = wvec[l]
                        if A[r_a][c_a] != B[k][l]:
                            isSame = False
                            break
                            
                if isSame:
                    print("Yes")
                    return 0

    print("No")
    return 0



def input_args():
    h1, w1 = map(int, input().split())
    A = []
    for _ in range(h1):
        a = list(map(int, input().split()))
        A.append(a)
    
    h2, w2 = map(int, input().split())
    B = []
    for _ in range(h2):
        b = list(map(int, input().split()))
        B.append(b)
    
    return [h1, w1, A, h2, w2, B]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)