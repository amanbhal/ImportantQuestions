"""
You are given an array containing colors (R,G,Y), find a couple(both colors adjacent to each other) and remove the
pair. After removal of this pair if there are further couple of this color then remove them also and so on.

example:
R G B B G R Y
=> removing B B
R G G R Y
=> removing G G
R R Y
=> removing R R
Y
"""

def removeCouple(arr):
    #convert it to string
    #color = "".join(arr)
    prevLength = None
    count = 0
    #while there is no change in length
    while prevLength!=len(arr):
        prevLength = len(arr)
        i = 0
        while i<len(arr)-1:
            if arr[i]==arr[i+1]:
                arr = arr[:i]+arr[i+2:]
                count += 1
            else:
                i += 1
    print arr
    print count,"=>these many couples removed"

removeCouple(['R','G','B','B','G','R','Y'])
removeCouple(['Y','R','G','G','R','R','G','G','R','Y'])