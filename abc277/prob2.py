

def solve(N, lst):
    for i, s in enumerate(lst):
        if s[0] not in ['H', 'D', 'C', 'S']:
            print('No')
            return 

        if s[1] not in [ 'A' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , 'T' , 'J' , 'Q' , 'K']:
            print('No')
            return 

        if s in lst[:i] or s in lst[i+1:]:
            print('No')
            return
    print('Yes')
            
    return 0



def input_args():
    N = int(input())
    lst = []
    for _ in range(N):
        s = input()        
        lst.append(s)
    return [N, lst]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)