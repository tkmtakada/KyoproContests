

def solve(N, animals):
    max_time = animals[-1][0]
    dp = [['#' for _ in range(max_time+1)] for _ in range(5)]
    dp[0][0] = 0

    top4 = [0, -float('inf'), -float('inf'), -float('inf')]  # (0, 0)の 0
    for animal in animals:
        t, x, a = animal
        # print(x,t)
        dp[x][t] = findMaxReachablePoint(dp, t, x, top4) + a
        top4.sort()
        if dp[x][t] > top4[0]:
            top4.append(dp[x][t])
            top4.sort()
            top4 = top4[1:]
    top4.sort()
    print(top4[-1])
    return 0

def findMaxReachablePoint(dp, t, x, top4):
    """
    それまでの最高点Top4をｑに保持しておく
    Unreachable Zoneに入っているものを除き、
    ｑの最高値が、Reachableなもの
    """
    Unreachable =      [(t-3, x-4), (t-2, x-4), (t-1, x-4), 
                                    (t-2, x-3), (t-1, x-3),  
                                                (t-1, x-2), 
                                                (t-3, x+4), 
                                    (t-2, x+4), (t-1, x+4), 
                        (t-2, x+3), (t-1, x+3), (t-1, x+2)]
    numsInUnreachable = []
    for t, x in Unreachable:
        if t >= 0 and x >= 0 and x <= 4:
            if dp[x][t] != '#':
                numsInUnreachable.append(dp[x][t])
    
    if len(numsInUnreachable) == 0:
        return max(top4)
    else: 
        top4.sort()
        for i in reversed(range(4)):
            if top4[i] in numsInUnreachable:
                pass
            else:
                return top4[i]





def input_args():
    N = int(input())
    animals = []
    for _ in range(N):
        t, x, a = map(int, input().split())
        animals.append([t, x, a])
    return [N, animals]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)