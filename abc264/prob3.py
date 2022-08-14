

def solve(h1, w1, A, h2, w2, B):
    cand = getCand(A, B, 0, 0, h2)
    q = cand

    while len(q) > 0:
        for _ in range(len(q)):
            a_idx, b_idx = q.pop(0)  # (Aのどの行を使ってるか、Bの何行目か
            cand = getCand(A, B, b_idx+1, a_idx+1, h2)
            q.extend(cand)
        
        if b_idx == h2-1:
            print('Yes')
            return 
    print('No')

def getCand(A, B, b_idx, min_i, h2):  # min_i以上のiで探す
    if b_idx > h2 - 1:
        return []
    
    nextRowCand = []
    for i in range(min_i, len(A)):
        a = A[i]
        b_lst = B[b_idx]

        # b が aに含まれるかを検証
        b = B[b_idx]
        k = 0
        for j in range(len(a)):
            if a[j] == b[k]:
                k += 1
                if k > len(b) - 1:
                    nextRowCand.append((i, b_idx))
                    break
        
        """
        for j in range(len(a)):
            if a[j] == b_lst[0]:
                b_lst.pop(0)
            if len(b_lst) == 0:
                nextRowCand.append((i, b_idx))
                break
        """
    return nextRowCand
        
    



def input_args():
    h1, w1 = map(int, input().split())
    A = []
    for _ in range(h1):
        a = list(map(int, input().split()))
        A.append(a)
    
    h2, w2 = map(int, input().split())
    B = []
    for _ in range(h2):
        b = list(map(int, input().split()))
        B.append(b)
    
    return [h1, w1, A, h2, w2, B]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)