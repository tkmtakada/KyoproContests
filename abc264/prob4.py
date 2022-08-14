

def solve(S):
    atcoder = list("atcoder")
    s = list(S)
    cnt = 0
    for i, char in enumerate(atcoder):
        cur_idx = s.index(char)
        cnt += cur_idx - i
        s = move(s, cur_idx, i)
    print(cnt)

def move(s, cur, dest):

    for i in range(cur - dest):
        s[cur-1-i], s[cur-i] = s[cur-i], s[cur-1-i]  # swap

    return s

def input_args():
    S = input()
    return [S]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)