import sys
def input_file():
    with open(str(sys.argv[1]), 'r') as f:
        points = []
        for line in f:
            points.append([float(g) for g in line.split()])
        return points
        
def distance(p_1, p_2):
    x_1, y_1 = p_1
    x_2, y_2 = p_2
    return ((x_2 - x_1)**2 + (y_2 - y_1)**2)**.5
    
def minCross(points, mid, d): 
    #find the x position of the middle point
    midx = points[mid][0]
    #stores the points nearest to the middle point
    stripe = []
    #make sure the new distance for the middle section is smaller than the minimum distance from L and R 
    for p in points:
        if abs(p[0] - midx) < d:
            stripe += [p]
    #sort by y values
    stripe.sort(key = lambda p: p[1])
    #check all the points within 8 y placements of each other in list stripe
    for i in range(0, len(stripe)):
        #this nestled loop is constant
        for j in range(i+1, min(i+8,len(stripe))):
            d = min(d, distance(points[i], points[j]))
    return d
    
def minSubarray(points):
    if len(points) == 1:
        return float("inf")
    if len(points) == 2:
        return distance(points[0], points[1])
    mid = len(points) / 2
    L_min = minSubarray(points[:mid])
    R_min = minSubarray(points[mid:])
    d = min(L_min, R_min)
    M_min = minCross(points, mid, d)
    return min(d, M_min)
    
if len(sys.argv) != 2:
    print "You must add a path to the file\n"
    sys.exit()
    
points = input_file()
points_x = sorted(points, key = lambda p: p[0])
print minSubarray(points_x)