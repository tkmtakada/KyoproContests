

def solve(X, Y, Z):
    # ゴールまで壁に邪魔されない場合
    if X * Y < 0 or Y**2 > X**2:
        print(abs(X))
    elif Z * Y < 0 or Y**2 > Z**2:  # ゴールまでは壁に邪魔されるが、ハンマーまでは邪魔されない場合
        print(abs(Z) + abs(X-Z))
    else:
        print(-1)
    
    return 0



def input_args():
    X, Y, Z = map(int, input().split())
    return [X, Y, Z]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)