"""
普通にBFS（もちろん、一度通った場所は記録した）
をやると、TLEのケースが4つもある
"""

def main(N, ladder, stories):
    lst_stories = list(stories)
    lst_stories.sort(reverse=True)
    for s in stories:
        if solve(N, ladder, s):
            print(s)
            return
    print(1)
    return

def solve(N, ladder, start):
    # bfs
    maxHeight = 1
    visited = set([])
    q = [start]    
    while len(q) > 0:
        len_q = len(q)
        for _ in range(len_q):
            elt = q.pop(0)
            # maxHeight = max(maxHeight, elt)
            if elt == 1: return True

            visited.add(elt)
            if elt in ladder:
                nextCands = ladder[elt]
                q.extend([elt for elt in nextCands if elt not in visited])
            else:
                pass
    # print(maxHeight)
    return False
    return 0



def input_args():
    N = int(input())
    stories = set([])
    ladder = {}
    for _ in range(N):
        a, b = map(int, input().split())
        stories.add(a)
        stories.add(b)
        if a in ladder:
            ladder[a].append(b)
        else:
            ladder[a] = [b]
        if b in ladder:
            ladder[b].append(a)
        else:
            ladder[b] = [a]
        
    return [N, ladder, stories]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    main(*args)