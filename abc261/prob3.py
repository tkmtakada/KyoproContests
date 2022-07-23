

def solve(N, S, ans):
    for elt in ans:
        print(elt)
    return 0

def input_args():
    N = int(input())
    S = []
    ans = []
    mp = {}
    for _ in range(N):
        s = input()
        # S.append(s)
        if s in mp:
            ans.append(s + "({})".format(mp[s]))
            mp[s] += 1
        else:
            mp[s] = 1
            ans.append(s)
        
    return [N, S, ans]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)