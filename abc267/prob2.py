

def solve(S):
    if S[0] == 1:
        print('No')
        return 

    row1 = [S[6]]
    row2 = [S[3]]
    row3 = [S[1], S[7]]
    row4 = [S[0], S[4]]
    row5 = [S[2], S[8]]
    row6 = [S[5]]
    row7 = [S[9]]
    rows = [row1, row2, row3, row4, row5, row6, row7]
    left = None
    for i, row in enumerate(rows):
        if not isEmpty(row):  # exist
            left = i
            break
    right = None
    for j, row in enumerate(reversed(rows)):
        if not isEmpty(row):  # exist
            right = 6 - j
            break
    
    # both left , right are None
    if left is None:  # right should also be None
        print('No')
        return
    
    # left == right
    if left == right or (left + 1) == right:
        print('No')
        return

    # if there is emmpty row(s) between left and right, it 
    emptyRowExit = False
    for k in range(left+1, right):
        emptyRowExit += isEmpty(rows[k])

    if emptyRowExit:
        print('Yes')
        return 
    else:
        print('No')
        return 
    return 0

def isEmpty(lst):
    if sum(lst) == 0:
        return True
    else:
        return False
    


def input_args():
    S = list(map(int, list(input())))
    return [S]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)