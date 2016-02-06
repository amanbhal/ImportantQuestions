"""
Given a collection of intervals, merge all overlapping intervals.

For example,
 Given [1,3],[2,6],[8,10],[15,18],
 return [1,6],[8,10],[15,18].

"""

#=> main idea is to sort the intervals according to the starting value
#=> maintain a minimum and a maximum. Iterate through each interval object in the list of intervals and
#   compare their starting value with the minimum and maximum. If it falls between the range then update
#   maximum(if needed). If it doesnt fall into the range then make a new interval with existing mini amd maxi
#   values and insert it into result list and then update the mini and maxi.

class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    if len(intervals)==0 or len(intervals)<2:
        return intervals
    #Sorting the intervals according to there starting value (this is important).
    intervals = sorted(intervals,key= lambda interval: interval.start)
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

result = merge(intervals)
#printing the result
for i in result:
    print "["+str(i.start)+","+str(i.end)+"]"