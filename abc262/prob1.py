

def solve(Y):
    q = Y % 4
    if q == 2:
        print(Y)
    elif q == 1:
        print(Y + 1)
    elif q == 0:
        print(Y + 2)
    elif q == 3:
        print(Y + 3)
    



def input_args():
    Y = int(input())
    return [Y]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)