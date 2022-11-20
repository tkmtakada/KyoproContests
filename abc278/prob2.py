

def solve(H, M):
    cur = (H, M)
    while True:
        isMisleading = checkCurTime(cur)
        if isMisleading:            
            print(*cur)
            return  # terminate program
        else:
            cur = advanceTime(cur)

def advanceTime(cur):
    h, m = cur
    newM = m+1
    newH = h
    if newM >= 60:
        newH = h + 1
        newM = 0
    
    if newH >= 24:
        newH = 0
    return (newH, newM)


def checkCurTime(time):
    H, M = time
    if H <= 9:
        str_H = '0' + str(H)
    else:
        str_H = str(H)
    
    if M <= 9:
        str_M = '0' + str(M)
    else:
        str_M = str(M)

    str_newH = str_H[0] + str_M[0]
    str_newM = str_H[1] + str_M[1]
    newH = int(str_newH)
    newM = int(str_newM)

    if (0<=newH) and (newH<=23) and (0<=newM) and (newM<=59):
        return True  # misleading
    else:
        return False
    
    




def input_args():
    H, M = map(int, input().split())
    return [H, M]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)