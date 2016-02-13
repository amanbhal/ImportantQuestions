"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed
as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to
finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses,
return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course
order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses
1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct
ordering is[0,2,1,3].

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices.
"""

#   As this question requires the correct order of courses to be taken so that we can complete all the courses
#   therefore we have to make a graph i.e. adjacency matrix and then use DFS to find topological order.

def findOrder(numCourses, prerequisites):
    if len(prerequisites)==0:
        return [j for j in range(numCourses)]
    global adjMat
    global flag
    flag = False
    adjMat = {}
    for j in range(numCourses):
        adjMat.update({j:[]})
    for j in prerequisites:
        adjMat[j[1]].append(j[0])
    global color
    color = ["white" for j in range(numCourses)]
    global i
    i = numCourses-1
    global S
    S = [None for x in range(numCourses)]
    for v in range(numCourses):
        if color[v]=="white":
            DFS(v)
    if flag:
        return []
    else:
        return S

def DFS(v):
    global color
    global adjMat
    global i
    global flag
    color[v] = "grey"
    for u in adjMat[v]:
        if color[u]=="white":
            DFS(u)
        elif color[u]=="grey":
            #flag raised upon detecting a cycle in the graph
            flag = True
            return []
    color[v] = "black"
    S[i] = v
    i -= 1