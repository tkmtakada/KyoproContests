
"""
これ、実は
n = int(input())
s = input()
print("Yes" if (s[0] == "B" or s[-1] == "A") and s != "BA" else "No")

で終わる問題で、テストケースには超大きい文字が入っていて、おそらくメモリリークを起こしてREが起きていた。
"""

def solve(N, S):
    if isPalindrome(S):
        print('Yes')
    else:
        print('No')
    return 0

def isPalindrome(s):
    # print(s)
    # 終了条件
    if len(s) == 0:
        return True
    if len(s) == 1:
        return True
    elif len(s) == 2 and s[0]==s[1]:
        return True
    elif len(s) == 2 and s[0]!=s[1]:
        return False

    # 以下は基本的にsの長さが3以上の時
    if s[0] == 'A' and s[-1] == 'A':
        # print("hi1")
        return isPalindrome(s[1:-1]) or isPalindrome('B'+s[2:-1])
    elif s[0] == 'A' and s[-1] == 'B':
        # print("hi2")
        return False
    elif s[0] == 'B' and s[-1] == 'A':
        # print("hi3")
        return isPalindrome(s[1:-2]+'A') or isPalindrome('B'+s[2:-1])
    elif s[0] == 'B' and s[-1] == 'B':
        # print("hi4")
        return isPalindrome(s[1:-1]) or isPalindrome(s[1:-2]+'A')
        



def input_args():
    N = int(input())
    S = input()
    return [N, S]

def test():
    print("THIS IS TEST!")
    N = 6
    # S = 'BAABAA'
    S = 'BBBBAAB'
    return [N, S]

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)