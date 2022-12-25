

def solve(N, M, lst):
    counter = 0
    for first in range(N-1):
        for second in range(first+1, N):            
            if canSolveAll(lst[first], lst[second], M):
                counter += 1
    print(counter)


    return 0

def canSolveAll(s1, s2, M):
    flag = True
    for q in range(M):
        flag *= (s1[q] == 'o' or s2[q] == 'o')    
    return flag


def input_args():
    N, M = map(int, input().split())
    lst = []
    for _ in range(N):
        s = input()
        lst.append(s)
    return [N, M, lst]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)