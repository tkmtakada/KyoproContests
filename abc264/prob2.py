

def solve(R, C):
    x = C - 8
    y = R - 8

    c = max(abs(x), abs(y))
    if c % 2 == 0:
        print("white")
    else:
        print("black")




def input_args():
    R, C = map(int, input().split())
    return [R, C]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)