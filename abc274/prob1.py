

def solve(A, B):
    rate = 1.0 * B / A
    
    if rate == 1.0:
        print('1.000')
        return 
    elif rate == 0.0:
        print('0.000')
        return 
    
    val = rate * 1000
    my_round_int = lambda x: int((x * 2 + 1) // 2)    
    val2 = my_round_int(val)
    print("0." + str(val2))
    return 



def input_args():
    A, B = map(int, input().split())
    return [A,B]

def test():
    for a in range(1, 11):
        for b in range(a+1):
            solve(a, b)
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)
    # test()