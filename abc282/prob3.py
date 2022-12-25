

def solve(N, S):
    lst_S = list(S)
    inBetween = False
    for idx, s in enumerate(lst_S):
        # print(idx, inBetween) 
        if not inBetween and s == '"':
            inBetween = True        
        elif inBetween and s =='"':
            inBetween = False
        elif not inBetween and s == ',':
            lst_S[idx] = '.'
            
    
    print("".join(lst_S))

    return 0



def input_args():
    N = int(input())
    S = input()
    return [N, S]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)