#formulatask1q7
n=int(input("Enter number of coordinates"))
points=[]
for i in range(n):
    x=int(input("Enter x-coordinate"))
    y=int(input("Enter y-coordinate"))
    points.append([x,y])
x0=int(input("Enter x-coordinate of reference point"))
y0=int(input("Enter y-coordinate of reference point"))
def distance(point):
    return (point[0]-x0)**2+(point[1]-y0)**2
distance_point=[]
for point in points:
    d=distance(point)
    distance_point.append([d, point])
    distance_point.sort()
sorted_points=[]
for item in distance_point:
     sorted_points.append(item[1])
print(sorted_points)
