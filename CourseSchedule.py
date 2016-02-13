"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed
as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you
should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices.
"""

#since we dont have to find the correct ordering of the courses therefore we can simply use BFS

def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    if numCourses==0 or len(prerequisites)==0:
        return True
    #make a counter for prequisites
    counter = [0 for i in range(numCourses)]
    #fill counter
    for i in range(len(prerequisites)):
        counter[prerequisites[i][0]] += 1
    #make a queue of courses having no prerequisites
    noPre = []
    for i in range(len(counter)):
        if counter[i]==0:
            noPre.append(i)
    #number of courses having no prerequisites
    numNoPre = len(noPre)
    while len(noPre)!=0:
        course = noPre.pop()
        #see if this course is able to satisfy prerequisite of any of the other courses or not
        for i in range(len(prerequisites)):
            if prerequisites[i][1]==course:
                counter[prerequisites[i][0]] -= 1
                if counter[prerequisites[i][0]]==0:
                    numNoPre += 1
                    noPre.append(prerequisites[i][0])
    return numNoPre==numCourses

print canFinish(2,[[1,0],[0,1]])