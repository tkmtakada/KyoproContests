

def solve(A, B, C, D):
    lst = [A, B, C, D]

    isConvex = True
    for i in range(4):
        node1, node2 = lst[i%4], lst[(i+1)%4]
        node3, node4 = lst[(i+2)%4], lst[(i+3)%4]

        #  check if line on which node1 and nod2 exist is vertical or not
        if node1[0] == node2[0]:
            x = node1[0]
            if (node3[0] - x) * (node4[0] - x) < 0:
                # isConvex = False
                print('No')
                return 
        else:
            def line(x):
                return (node2[1]-node1[1]) / (node2[0]-node1[0]) * (x - node1[0]) + node1[1]            
            if (node3[1] - line(node3[0])) * (node4[1] - line(node4[0])) < 0:
                # isConvex = True
                print('No')
                return 
    print('Yes')
            



def input_args():
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))
    return [A, B, C, D]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)