

def solve(k):
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(s[:k])
    return 0



def input_args():
    k = int(input())
    return [k]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)