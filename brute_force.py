#http://stackoverflow.com/questions/6583573/how-to-read-numbers-from-file-in-python
def input_file():
    with open('input_10.txt') as f:
        points = []
        for line in f:
            points.append([float(g) for g in line.split()])
        return points
            
def distance(p_1, p_2):
    x_1, y_1 = p_1
    x_2, y_2 = p_2
    return ((x_2 - x_1)**2 + (y_2 - y_1)**2)**.5
         
def min_dist(points):
    shortest = distance(points[0], points[1])
    n = len(points)
    for p_i in range(0,n):
        for p_j in range(p_i+1, n):
            shortest = min(distance(points[p_i], points[p_j]), shortest)
    return shortest
    
points = input_file()
points_x = sorted(points, key = lambda p: p[0])
print min_dist(points_x)