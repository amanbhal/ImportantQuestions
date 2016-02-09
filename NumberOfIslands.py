"""
Given a 2d grid map of 1s (land) and 0s (water), count the number of islands. An island is surrounded
by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four
edges of the grid are all surrounded by water.
"""

#=> Simple idea. Iterate through the whole matrix and whenever you come accross a 1 increase the count and sink
#   the whole island iteratively.

def numIslands(grid):
    global result
    result = []
    result = grid
    count = 0
    for i in range(len(result)):
        for j in range(len(result[0])):
            if result[i][j]==1:
                count += 1
                sinkIsland(i,j)
    return count

def sinkIsland(i,j):
    global result
    if i<0 or j<0 or i>=len(result) or j>=len(result[0]):
        return
    if result[i][j]==0:
        return
    if result[i][j]==1:
        result[i][j] = 0
    sinkIsland(i-1,j)
    sinkIsland(i,j-1)
    sinkIsland(i+1,j)
    sinkIsland(i,j+1)

print numIslands([[1,1,0,0,0,1],[1,1,1,0,0,0]])