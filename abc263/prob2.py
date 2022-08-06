

def solve(N, P):
    parents = [[] for _ in range(N+1)]
    for i, p in enumerate(P):
        child = i+2
        parents[child].append(p) 
    
    q = parents[N]
    counter = 1
    while len(q) > 0:
        len_q = len(q)
        for i in range(len_q):
            prt = q.pop(0)
            if prt == 1:
                print(counter)
                return
            q.extend(parents[prt])
        
        counter += 1
    # print("ERROR")




def input_args():
    N = int(input())
    P = list(map(int, input().split()))
    return [N, P]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)