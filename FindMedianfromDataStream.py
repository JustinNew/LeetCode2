# 295. Find Median from Data Stream

# Google Tag

'''
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
'''

class MedianFinder:

    import heapq

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.h1 = []
        self.h2 = []


    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        
        if len(self.h1) == len(self.h2):
            heapq.heappush(self.h1, -1 * num)
            t = heapq.heappop(self.h1) * -1
            heapq.heappush(self.h2, t)
        else:
            heapq.heappush(self.h2, num)
            t = heapq.heappop(self.h2)
            heapq.heappush(self.h1, t * -1)

        return

    def findMedian(self):
        """
        :rtype: float
        """
    
        if len(self.h1) == len(self.h2):
            t1 = -1 * self.h1[0]
            t2 = self.h2[0]
            return (t1 + t2) / 2
        else:
            return self.h2[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
