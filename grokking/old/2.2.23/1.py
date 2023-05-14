from heapq import *


class MedianOfAStream:
    minheap, maxheap = [], []

    def insert_num(self, num):
        if not self.maxheap or -self.maxheap[0] >= num:
            heappush(self.maxheap, -num)
        else:
            heappush(self.minheap, num)

        if len(self.maxheap) > len(self.minheap) + 1:
            heappush(self.minheap, -heappop(self.maxheap))
        elif len(self.maxheap) < len(self.minheap):
            heappush(self.maxheap, -heappop(self.minheap))

    def find_median(self):
        if len(self.maxheap) == len(self.minheap):
            return -self.maxheap[0] / 2.0 + self.minheap[0] / 2.0
        return -self.maxheap[0] / 1.0


def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))


main()
