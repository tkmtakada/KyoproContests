

def solve(lst):
    mod = 998244353
    a, b, c = lst[:3]
    d, e, f = lst[3:]
    ans = (a % mod) * (b % mod) * (c % mod) - (d%mod) * (e%mod) * (f%mod)
    
    print(ans % mod)
    return 0



def input_args():
    lst = list(map(int, input().split()))
    return [lst]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)