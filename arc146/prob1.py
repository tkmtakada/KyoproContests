import heapq

# MAXV = 10 ** 6 - 1

def solve(N, strA):
    mp = {}
    for num in strA:
        length = len(num)
        if length in mp:
            mp[length].append(int(num))
        else:
            mp[length] = [int(num)]
    
    key_lst = list(mp.keys())
    
    cand = []
    max_length = max(key_lst)
    idx = key_lst.index(max_length)
    key_lst.pop(idx)
    cand.extend(mp[max_length])

    if len(cand) == 2:
        # 二番目に長い数字を、最大2コマでとる

        # top2 のｋeyのIndexをとる
        max_length = max(key_lst)
        idx = key_lst.index(max_length)
        key_lst.pop(idx)
        lst = mp[max_length]
        cand.append(max(lst))
    elif len(cand) == 1:
        max_length = max(key_lst)
        idx = key_lst.index(max_length)
        key_lst.pop(idx)
        lst = mp[max_length]
        lst.sort(reverse=True)
        if len(lst) == 2:
            cand.extend(lst)
        elif len(lst) == 1:
            cand.extend(lst)
            # 第三個目をいれる
            max_length = max(key_lst)
            idx = key_lst.index(max_length)
            key_lst.pop(idx)
            lst = mp[max_length]
            lst.sort(reverse=True)
            cand.append(lst[0])
        else:
            cand.extend(lst[:2])




    cand = [str(num) for num in cand]    


    q = []
    heapq.heapify(q)
    for num in cand:
        v = (-process(num), num)
        heapq.heappush(q, v)
    ans = []
    for i in range(3):
        v = heapq.heappop(q)
        ans.append(v[1])
    
    print("".join(ans))
    return 0
    
    

def process(num):
    num_digit = len(num)
    topDigit = num[0]
    mp = {}
    for _ in range(6-num_digit):
        num += topDigit

    return int(num)


def input_args():
    N = int(input())
    strA = list(input().split())
    # A = list(map(int, input().split()))
    return [N, strA]

def test():
    N = 4
    A = [412, 4151, 75, 62]

    return [N, [str(num) for num in A]]

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)