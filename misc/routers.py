"""
Tommy Janna
Oct. 3, 2021
routers.py
COMP3203

Given a complete binary tree, what is the average distance between two nodes
where the path must first pass through the root node before reaching the
destination node.
""" 
import math
import random

height = 3
nRouters = 2 ** height - 1
accuracy = 10000
routers = {}
for i in range(1, nRouters + 1):
    routers[i] = math.floor(math.log2(i))

count = 0

for i in range(accuracy):
    u = random.randint(1, len(routers)) # sending router
    v = random.randint(1, len(routers)) # receiving router
    
    count += routers[u] + routers[v]
    

print('For a tree of height, ' + str(height) + ', average is: ' + str(count / accuracy))
