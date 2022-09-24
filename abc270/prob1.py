

def solve(A, B):
    # takahashi
    isCorrect_t = [0, 0, 0]  # 1p, 2p, 4p
    isCorrect_t[2] = A // 4
    A1 = A % 4
    isCorrect_t[1] = A1 // 2
    A2 = A1 % 2
    isCorrect_t[0] = A2

    # aoki
    isCorrect_a = [0, 0, 0]  # 1p, 2p, 4p
    isCorrect_a[2] = B // 4
    B1 = B % 4
    isCorrect_a[1] = B1 // 2
    B2 = B1 % 2
    isCorrect_a[0] = B2

    # sunuke
    points = 0
    for i in range(3):
        if isCorrect_t[i] or isCorrect_a[i]:
            points += 2 ** (i)
    print(points)

    return 0



def input_args():
    A, B = map(int, input().split())
    return [A, B]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)