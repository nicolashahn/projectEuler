# problem85.py
# Project Euler
# Nicolas Hahn

# int m, int n -> # of rectangles that can be made from m*n rectangle
def numRectangles(m,n):
    return (m*n*(m+1)*(n+1))//4

# int 'num' -> side length of first square that has >='num' rectangles
def getLargestSquareLength(num):
    rectNum = 0
    length = 0
    while rectNum < num:
        length += 1
        rectNum = numRectangles(length,length)
    return length

# int 'num' -> area of rectangle with closest to 'num' rectangles
def closestTo(num):
    rects = []
    # start from a square, work towards a 1*n rectangle
    length = getLargestSquareLength(num)
    for i in range(1,length+1):
        m = length-i
        n = m+1
        # find closest rectangle to 'num' with width m
        while numRectangles(m,n) < num and m > 0:
            n += 1
        # store both the >num rectangle and <num rectangle with width m
        rects.append((m,n,numRectangles(m,n)))
        rects.append((m,n-1,numRectangles(m,n-1)))
    # get closest number of rectangles, then compute area
    m,n,r = sorted(rects, key=lambda k: abs(k[2]-num))[0]
    return m*n

def main():
    # correct answer = 2772
    print(closestTo(2000000))

if __name__ == "__main__":
    main()