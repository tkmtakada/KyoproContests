

def solve(N, A):
    books = []
    stock = 0
    for a in A:
        if a in books:
            stock += 1            
        else:
            books.append(a)
    
    books.sort()

    for i in range(1, 10**9):
        if i in books:
            continue
        else:
            if stock >= 2:                
                stock -= 2
                continue
            elif stock == 1:
                
                if len(books) >= 1:
                    lastBook = books.pop()
                else:
                    break
                if lastBook > i:
                    stock -= 1
                    continue 
                else:
                    break
                    
            elif stock == 0:
                if len(books) >= 2:
                    books.pop()
                    lastBook = books.pop()
                else:
                    break
                
                if lastBook > i:
                    continue
                else:
                    break                    
                    
            
    print(i-1)
    return 0



def input_args():
    N = int(input())
    A = list(map(int, input().split()))
    return [N, A]

def test():
    return []

if __name__=="__main__":
    args = input_args()
    # args = test()
    solve(*args)