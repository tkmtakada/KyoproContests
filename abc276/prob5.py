
def solve(H, W, grid):
    def dfs(grid, i, j, islandId):
        # termination condition
        if i>=H or j>=W or i<0 or j<0 or (grid[i][j] != '.'):
            return
        # dfs
        grid[i][j] = islandId
        dfs(grid, i+1, j, islandId)
        dfs(grid, i, j+1, islandId)
        dfs(grid, i-1, j, islandId)
        dfs(grid, i, j-1, islandId)


    # 島を判別
    islandId = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '.':  # reclamaition
                dfs(grid, i, j, islandId)
                islandId += 1
            elif grid[i][j] == 'S':
                start_i, start_j = i,j

    # Sの四方で同じ島があればよい
    def getIslandId(grid, i, j):
        if i>=H or j>=W or i<0 or j<0:
            return None
        else:
            return grid[i][j]
    id1 = getIslandId(grid, start_i+1, start_j)
    id2 = getIslandId(grid, start_i, start_j+1)
    id3 = getIslandId(grid, start_i-1, start_j)
    id4 = getIslandId(grid, start_i, start_j-1)
    
    if id1 == id2 and id1 != None:
        print('Yes')
        return 
    if id1 == id3 and id1 != None:
        print('Yes')
        return 
    if id1 == id4 and id1 != None:
        print('Yes')
        return 
    if id2 == id3 and id2 != None:
        print('Yes')
        return 
    if id2 == id4 and id2 != None:
        print('Yes')
        return 
    if id3 == id4 and id3 != None:
        print('Yes')
        return 
    print('No')
    return 




def input_args():
    H, W = map(int, input().split())
    grid = []
    for _ in range(H):
        grid.append(list(input()))
    return [H, W, grid]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)