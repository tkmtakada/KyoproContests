

def solve(H, W, grid):
    ans = []
    for i in range(W):
        cnt = 0
        for j in range(H):
            if grid[j][i] == '#':
                cnt += 1
        ans.append(cnt)
    print(*ans)
    return 0



def input_args():
    H, W = map(int, input().split())
    grid = []
    for _ in range(H):
        r = input()
        grid.append(list(r))
    return [H, W, grid]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)