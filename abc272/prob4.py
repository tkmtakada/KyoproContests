import math

def solve(N, M):
    # find possible pairs of (i, j) s.t. i^2 + j^2 = M
    # i <= jとする    
    ij_lst = []
    mid = int(math.sqrt(M/2))
    for i in range(mid+1):  # 0, 1, ..., [sqrt(M/2)]
        j2 = M - i**2
        rt_j2 = judgeSquare(j2)
        if rt_j2:
            ij_lst.append([i, rt_j2])
    #深さ優先探索
    grid = [[-1 for _ in range(N)] for _ in range(N)]
    if len(ij_lst) == 0:
        myprint(grid)
    else:
        bfs(grid, ij_lst, N)
        myprint(grid)
        pass
    return 0

def bfs(grid, choices, N):

    q = [[0, 0]]
    step = 0
    while len(q) > 0:
        for i in range(len(q)):            
            top = q.pop(0)
            # 処理
            grid[top[0]][top[1]] = step
            # 追加
            cands = getCands(top[0], top[1], choices, grid, N)
            q.extend(cands)
        step += 1
    return grid
 
def getCands(i, j, choices, grid, N):
    next_pos = []
    for choice in choices:
        x, y = choice[0], choice[1]
        cands =[[i+x, j+y],
                [i+x, j-y],
                [i-x, j+y],
                [i-x, j-y],                
                [i+y, j+x],
                [i+y, j-x],
                [i-y, j+x],
                [i-y, j-x]]        
        for _i, _j in cands:
            if _i < 0 or _i >= N or _j < 0 or _j >= N or grid[_i][_j] != -1:
                pass
            else:    
                next_pos.append([_i, _j])
    return next_pos


def dfs(grid, i, j, step, choices, N):
    # 終了条件
    if i < 0 or i >= N or j < 0 or j >= N or grid[i][j] != -1:
        return 
    
    grid[i][j] = step
    print('cur step', step)
    # dfs
    for di, dj in choices:        
        dfs(grid, i+di, j+dj, step+1, choices, N)
        dfs(grid, i+di, j-dj, step+1, choices, N)
        dfs(grid, i-di, j+dj, step+1, choices, N)
        dfs(grid, i-di, j-dj, step+1, choices, N)        
        dfs(grid, i+dj, j+di, step+1, choices, N)
        dfs(grid, i+dj, j-di, step+1, choices, N)
        dfs(grid, i-dj, j+di, step+1, choices, N)
        dfs(grid, i-dj, j-di, step+1, choices, N)    

def judgeSquare(num):
    rt = int(math.sqrt(num))
    if rt**2 == num:
        return rt
    else:
        return False

def myprint(grid):
    for r in grid:
        print(*r)

def input_args():
    N, M = map(int, input().split())
    return [N, M]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)