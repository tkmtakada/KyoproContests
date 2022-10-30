
import numpy as np
def solve(grid):
    loc = []
    for i in range(9):
        for j in range(9):
            if grid[i][j] == '#':
                loc.append(np.array([i,j]))
    # loc_set = set(loc)
    def doesInclude(arr):
        for elt in loc:
            if (elt == arr).all():
                return True
        return False
    # --- 
    ans = 0  # 
    for i in range(len(loc)):
        for j in range(len(loc)):
            if i != j:
                pos1 = loc[i]
                pos2 = loc[j]            
                # 任意の2つを取った！
                vec12 = pos2-pos1
                vec13 = np.array([-vec12[1], vec12[0]])
                vec14 = vec12 + vec13
                pos3 = pos1 + vec13
                pos4 = pos1 + vec14
                if doesInclude(pos3) and doesInclude(pos4):
                    ans += 1        

                vec13_ = np.array([vec12[1], -vec12[0]])
                vec14_ = vec12 + vec13_
                pos3_ = pos1 + vec13_
                pos4_ = pos1 + vec14_
                if doesInclude(pos3_) and doesInclude(pos4_):
                    ans += 1
    print(ans // 8)
    return 0



def input_args():
    grid = []
    for _ in range(9):
        s = list(input())
        grid.append(s)
    return [grid]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)