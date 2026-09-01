#formulatask1q8
import csv
cone=[]
with open("cone.csv","r") as file:
    reader=csv.DictReader(file)
    for row in reader:
     row["x"]=float(row["x"])
     row["y"]=float(row["y"])
     cone.append(row)
def distance(cone):
 return cone["x"]**2+cone["y"]**2
cone.sort(key=distance)
blue=[]
yellow=[]
for c in cone:
    if c["colour"]=="blue":
     blue.append(c)
    else:
     yellow.append(c)
centreline=[]
for b in blue:
    nearest=None
    min_dist=float("inf")
    for y in yellow:
        d=(b["x"]-y["x"])**2+(b["y"]-y["y"])**2
        if d<min_dist:
         min_dist=d
         nearest=y
    mid=[(b["x"]+nearest["x"])/2,(b["y"]+nearest["y"])/2]
    centreline.append(mid)
with open("centreline_cone.csv","w",newline="") as file:
 writer=csv.writer(file)
 writer.writerow(["x","y"])
 for point in centreline:
  writer.writerow(point)
print(centreline)
    

