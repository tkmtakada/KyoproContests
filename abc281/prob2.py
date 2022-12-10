

def solve(S):
    alph = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    str_numbers = list("0123456789")
    cond0 = (len(S) == 8)
    if not cond0:
        print("No")
        return

    cond1 = S[0] in alph
    if not cond1:
        print("No")
        return

    for s in S[1:7]:
        if s not in str_numbers:
            print("No")
            return
    num = int(S[1:7])    
    cond2 = (num >= 100000) and (num <= 999999)
    if not cond2:
        print("No")
        return
    
    cond3 = S[7] in alph
    if not cond3:
        print("No")
        return
    
    print("Yes")
    return 0



def input_args():
    S = input()
    return [S]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)