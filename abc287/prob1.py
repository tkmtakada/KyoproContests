

def solve(N, lst, counter):    
    thr = N // 2 + 1
    if counter >= thr:
        print('Yes')
    else:
        print('No')
    return 0



def input_args():
    N = int(input())
    lst = []
    counter = 0
    for _ in range(N):
        elt = input()
        if elt == 'For':
            counter += 1
        lst.append(elt)
    return [N, lst, counter]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)