

def solve(S):
    if S == 'Monday':
        print(5)
    elif S == 'Tuesday':
        print(4)
    elif S == 'Wednesday':
        print(3)
    elif S == 'Thursday':
        print(2)
    elif S == 'Friday':
        print(1)
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