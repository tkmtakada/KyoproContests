"""
できるだけ、手札を捨てたいゲーム
おんなじカードは全部消せるし、Modで一つ違いなのも消せるときに、
"""

def solve(N, M, A):
    mp = {}
    for a in A:
        a_mod = a % M
        if a_mod in mp:
            mp[a_mod] += 1
        else:
            mp[a_mod] = 1 
    # find sequence
    key_lst = sorted(list(mp.keys()))
    groups = []
    grp = [key_lst[0]]
    for i in range(1, len(key_lst)):
        if key_lst[i] == key_lst[i-1] + 1:
            grp.append(key_lst[i])
        else:
            groups.append(grp)
            grp = [key_lst[i]]
    groups.append(grp)

    
    
    return 0



def input_args():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    return [N, M, A]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)