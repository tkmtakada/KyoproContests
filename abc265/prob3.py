

def solve(H, W, grid):
    cur_pos = (0, 0)
    visited = set([])
    while True:
        visited.add(cur_pos)
        nx = move(grid, cur_pos, H, W)
        if nx != cur_pos and nx in visited:
            print(-1)
            return 
            
        if nx == cur_pos:
            print(cur_pos[0]+1, cur_pos[1]+1)
            return 
        cur_pos = nx

def move(grid, cur_pos, H, W):
    x, y = cur_pos
    d = grid[x][y]
    nx = cur_pos
    if d == 'U' and x != 0:
        nx = (x-1, y)
    elif d == 'D' and x != H-1:
        nx = (x+1, y)
    elif d == 'L' and y != 0:
        nx = (x, y-1)
    elif d == 'R' and y != W-1:
        nx = (x, y+1)
    return nx

def input_args():
    H, W = map(int, input().split())
    grid = []
    for _ in range(H):
        lst = list(input())
        grid.append(lst)
    return [H, W, grid]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)