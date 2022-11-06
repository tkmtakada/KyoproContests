

def solve(s):
    idx = -1
    for i, ch in enumerate(s):
        if ch == 'a':
            idx = i+1
    print(idx)
    return 0



def input_args():
    s = input()    
    return [s]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)