def watchDog():
    n = int(input())
    for i in range(x):
        s, h = map(int, input().split())
        minimumXY = (float('inf'), float('inf') )
        for j in range(h):
            x, y = map(int, input().split())
            if x < minimumXY[0] or (x == minimumXY and y < minimumXY[1]):
                minimumXY = (x, y)
                
            


watchDog()