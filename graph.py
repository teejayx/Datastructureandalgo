""""
A graoh models a set of connections
Graphs are made up of nodes and edges 
nodes can be directly connected to many other nodes via the egde

graphs are way to model how differernt things are connected to one another 

A queue works exactly lie it does in real life which is simlar to stacks 
it has 2 operations enqueue and dequeue FIFO first in first out 

Stack : LIFO datastructue  last in first our 

You also keep a queue of every person to search. 
Adding one person to the queue takes constant time: O(1).
 Doing this for every person will take O(number of people) total.
  Breadth-first search takes O(number of people + number of edges), 
  and it’s more commonly written as O(V+E) (V for number of vertices, 
  E for number of edges).


Recap
• Breadth-first search tells you if there’s a path from A to B.
• If there’s a path, breadth-first search will find the shortest path.
• If you have a problem like “find the shortest X,” try modeling your problem as a graph, and use breadth-first search to solve.
• A directed graph has arrows, and the relationship follows the direction of the arrow (rama -> adit means “rama owes adit money”).
• Undirected graphs don’t have arrows, and the relationship goes both ways (ross - rachel means “ross dated rachel and rachel dated ross”).
• Queues are FIFO (First In, First Out).
• Stacks are LIFO (Last In, First Out).
• You need to check people in the order they were added to the search list, so the search list needs to be a queue. Otherwise, you won’t get the shortest path.
• Once you check someone, make sure you don’t check them again. Otherwise, you might end up in an infinite loop.



"""

#breadfirst search 
# first degree connections 
from collections import deque
from operator import truediv

graph = {}
graph["you"] = ["alice", "bob", "claire"] 
graph["bob"] = ["anuj", "peggy"] 
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"] 
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(name):
    return name[-1] == 'm'




def search(name):
    search_queue = deque()                   #Create a new queue
    search_queue += graph["you"]             #Adds all of your neighours to the search queue
    searched = []                            # keep track of which people you have searched before.
    while search_queue:                      #while queue isnt empty 
        person = search_queue.popleft()      # grabs the first perosn off the queue
        if not person in searched:
            if person_is_seller(person):     #check whether the person is a mango seller
                print (person + " is a mango seller")
                return True
            else: 
                search_queue += graph[person]  #no, they arent, add all oof this person's friend to the search queue
                searched.append(person)
    return False




search("you")




