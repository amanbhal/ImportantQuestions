"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
 Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
 Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

"""

#=> Method 1
#       add the newInterval at the end of intervals and then sort the whole and then merge them.
#       But since the given list is already sorted therefore it does not make sense to sort it again.
#=> Method 2
#       add the newInterval at the correct position then apply merge on the whole list.

class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

def insert(intervals, newInterval):
    """
    :type intervals: List[Interval]
    :type newInterval: Interval
    :rtype: List[Interval]
    """
    #part 1 will be inserting the new interval at correct position
    if len(intervals)==0:
        return [newInterval]
    for i in range(len(intervals)):
        if intervals[i].start>newInterval.start:
            intervals = intervals[:i]+[newInterval]+intervals[i:]
            break
    if newInterval not in intervals:
        intervals.append(newInterval)
    return merge(intervals)

def merge(intervals):
    result = []
    mini = intervals[0].start
    maxi = intervals[0].end
    for i in range(1,len(intervals)):
        if intervals[i].start<=maxi and intervals[i].start>=mini:
            if intervals[i].end>maxi:
                maxi = intervals[i].end
        else:
            interval = Interval(mini,maxi)
            result.append(interval)
            mini = intervals[i].start
            maxi = intervals[i].end
    interval = Interval(mini,maxi)
    if interval not in result:
        result.append(interval)
    return result

intervals = []
intervals.append(Interval(1,6))
intervals.append(Interval(2,8))
intervals.append(Interval(10,12))
intervals.append(Interval(11,15))
intervals.append(Interval(16,18))

result = insert(intervals,Interval(14,20))
#printing the result
for i in result:
    print "["+str(i.start)+","+str(i.end)+"]"