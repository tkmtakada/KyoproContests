

def solve(cards):
    mp = {}
    for num in cards:
        if num in mp:
            mp[num] += 1
        else:
            mp[num] = 1

    # check
    keys = list(mp.keys())

    if len(keys) == 2:
        if mp[keys[0]] == 2 and mp[keys[1]] == 3:
            print('Yes')
            return 
        if mp[keys[0]] == 3 and mp[keys[1]] == 2:
            print('Yes')
            return
    
    print('No')
    return 



def input_args():
    cards = list(map(int, input().split()))
    return [cards]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)