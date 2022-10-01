

def solve(N):
    digit1 = N // 16
    digit2 = N % 16

    def convert(x):
        if x == 10:
            return 'A'
        elif x == 11:
            return 'B'
        elif x == 12:
            return 'C'
        elif x == 13:
            return 'D'
        elif x == 14:
            return 'E'
        elif x == 15:
            return 'F'
        else:
            return str(x)

    print(convert(digit1) + convert(digit2))
    return 0



def input_args():
    N = int(input())
    return [N]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)