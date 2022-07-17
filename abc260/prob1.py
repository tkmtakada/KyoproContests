

def solve(S):
    mp = {}
    for s in S:
        if s in mp:
            mp[s] += 1
        else:
            mp[s] = 1
    
    for k, v in mp.items():
        if v == 1:
            print(k)
            return k
    
    # ここまででreturn されていない場合、存在しないという事
    print(-1)
    return -1    



def input_args():
    S = input()
    return [S]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)