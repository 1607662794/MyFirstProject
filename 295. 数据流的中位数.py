import heapq


class MedianFinder:

    def __init__(self):

        self.queue_min = []
        self.queue_max = []
        heapq.heapify(self.queue_min)  # 两个都应该是小根堆
        heapq.heapify(self.queue_max)  # 两个都应该是小根堆
        self.num = 0

    def addNum(self, num: int) -> None:

        self.num += 1
        if len(self.queue_min) == 0:
            heapq.heappush(self.queue_min, -num)

        elif len(self.queue_max) == 0:
            if -self.queue_min[0] > num:
                heapq.heappush(self.queue_max, -heapq.heappop(self.queue_min))
                heapq.heappush(self.queue_min, -num)
            else:
                heapq.heappush(self.queue_max, num)

        elif self.num % 2 != 0:  # 加完当前值后总数为奇数
            if num <= self.queue_max[0]:
                heapq.heappush(self.queue_min, -num)
            else:
                heapq.heappush(self.queue_max, num)
                heapq.heappush(self.queue_min, -heapq.heappop(self.queue_max))
        else:  # 加完当前值后总数为偶数
            if num >= -self.queue_min[0]:
                heapq.heappush(self.queue_max, num)
            else:
                heapq.heappush(self.queue_min, -num)
                heapq.heappush(self.queue_max, -heapq.heappop(self.queue_min))
    def findMedian(self) -> float:
        if self.num % 2 == 0:
            return (-self.queue_min[0] + self.queue_max[0]) / 2
        else:
            return -self.queue_min[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()