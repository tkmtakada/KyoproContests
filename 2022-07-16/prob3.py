

def solve(N, K):
    if K > (N // 2):
        print(-1)
        return 
    
    # 階が存在する場合
    used = set([])
    ans = []
    for i in range(1, N+1):
        if i >= K + 1:
            # 下にいく
            if i - K not in used:
                ans.append(i-K)
            else:
                ans.append(i+K)
        else:
            ans.append(i + K)
            used.add(i+K)
    print(*ans)

def solve2(N, K):
    if K > (N // 2):
        print(-1)
        return 
    nums = list(range(1, N+1))

    ans = nums[K:] + nums[:K]
    print(*ans)





def input_args():
    N, K = map(int, input().split())
    return [N, K]

def test():
    return 

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve2(*args)