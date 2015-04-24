import sys
def input_file():
    #open file - with function opens and closes automatically
    with open(str(sys.argv[1]), 'r') as f:
        points = []
        for line in f:
            #add all the points in the file as a list of lists
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
    for i in points:
        if abs(i[0] - midx) < d:
            stripe += [i]
    #sort by y values
    stripe.sort(key = lambda i: i[1])
    #check all the points within 8 y placements of each other in list stripe
    for j in range(0, len(stripe)):
        #this nestled loop is constant
        for k in range(j+1, min(j+8,len(stripe))):
            d = min(d, distance(points[j], points[k]))
    return d
    
def minSubarray(points):
    #BaseCase: If only one point, there are no neighboring points
    if len(points) == 1:
        return float("inf")
    #BaseCase: If only two points, return the distance between them
    if len(points) == 2:
        return distance(points[0], points[1])
    #Use recursion to spilt the number of points in half
    mid = len(points) / 2
    L_min = minSubarray(points[:mid])
    R_min = minSubarray(points[mid:])
    #Find the minimum distance between the right and left, then check the stip in the middle
    d = min(L_min, R_min)
    M_min = minCross(points, mid, d)
    return min(d, M_min)
    
#Error checking the passed in arguments
if len(sys.argv) != 2:
    print "You must add a path to the file\n"
    sys.exit()
    
points = input_file()
points_x = sorted(points, key = lambda p: p[0])
#print minSubarray(points_x)
s = str(sys.argv[1])
s = s.replace(".txt", "_distance.txt")
with open(s, 'w+') as f:
    f.write(str(minSubarray(points_x)))