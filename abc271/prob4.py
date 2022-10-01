

def solve(N, S, cards):
    # mp : {value: [H/T, prevVal]
    dp = [{} for _ in range(N)]
    a0, b0 = cards[0]
    dp[0][a0] = ['H', 0]
    dp[0][b0] = ['T', 0]
    for i in range(1, N):
        a, b = cards[i]
        
        for val in dp[i-1].keys():
            dp[i][val + a] = ['H', val]
            dp[i][val + b] = ['T', val]    
    if S in dp[N-1]:
        print('Yes')

        eg = ""
        val = S
        for i in reversed(range(N)):
            info = dp[i][val]            
            eg = info[0] + eg
            val = info[1]
        print(eg)
    else:
        print('No')
    return 0



def input_args():
    N, S = map(int, input().split())
    cards = []
    for _ in range(N):
        a, b = map(int, input().split())
        cards.append([a,b])
    return [N, S, cards]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)