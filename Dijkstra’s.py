"""
this is used to find the fastest path ie shortest possibletime with weights i.e cost of time on edges 

"""


from collections import deque

graph = {}

graph["start"] = {} 
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {} 
graph["a"]["fin"] = 1
graph["b"] = {} 
graph["b"]["a"] = 3 
graph["b"]["fin"] = 5
graph["fin"] = {}      #The finish node doesn’t have any neighbors.

#cost table
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2 
costs["fin"] = infinity 

#parents 
parents = {} 
parents["a"] = "start" 
parents["b"] = "start" 
parents["fin"] = None

processed = []
print(graph["start"].keys())

