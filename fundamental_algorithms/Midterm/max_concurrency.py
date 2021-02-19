import heapq
from collections import defaultdict
from typing import List

start_and_end_times = [[4, 7], [2, 5], [1, 3], [5, 8]]


# test_tuples = [(1, 5), (3, 4), (3, 3), (2, 1), (2, 7), (1, 1)]
# heapq.heapify(test_tuples)


def max_concurrency_best(s):
    """Naive method to solve max_concurrency. Passes all tests!"""
    heap = []
    count = 0
    answer = 0
    heapq.heapify(s)
    if s:
        # from the min start time to the max end time
        for i in range(s[0][0], s[len(s) - 1][1]):
            for start_and_end_time in s:
                if i == start_and_end_time[0]:
                    count += 1
                    if len(heap) < 1:
                        heapq.heappush(heap, count)
                    elif len(heap) == 1:
                        # fast push, then pop
                        heapq.heappushpop(heap, count)
                    else:
                        heapq.heappop(heap)
                elif i == start_and_end_time[1]:
                    count -= 1
        if heap:
            answer = heap[0]
    return answer


def max_concurrency_attempt_1(s):
    """Efficient method to solve max_concurrency. Passes 4 tests."""
    heap = []
    start = 0
    end = 1
    heapq.heapify(s[:])
    if s:
        count = len(s)
        heapq.heappush(heap, s[0])
        for i in range(len(s)):
            top = s[0]
            if top[end] < s[i][start]:
                heapq.heappush(heap, s[i])
                count -= 1
            elif top[end] < s[i][end]:
                # top[end] = s[i][end]
                heapq.heappop(heap)
                heapq.heappush(heap, top)
                count += 1
    else:
        count = 0
    return count


def max_concurrency_attempt_2(s):
    """Efficient method to solve max_concurrency. Doesn't even compile."""
    import heapq
    h = []
    heapq.heappush(h, 10000)
    res = 0
    for (start, end) in s:
        while heapq.nsmallest(1, h)[0] < s:
            heapq.heappop(h)
        res = res + len(h) - 1
        heapq.heappush(h, end)
    return res


def max_concurrency_attempt_3(s):
    """Fails 9 tests."""
    es = []
    for start, end in s:
        es.append((start, -1))
        es.append((end, 1))
    es.sort()
    result = 0
    n = 0
    for start, s in es:
        if s == -1:
            result += n
        n -= s
    return result


def max_concurrency_attempt_4(intervals):
    """Fails all tests."""
    intervals = sorted(intervals)
    first_start, first_end = intervals[0]
    current_intervals = []
    heapq.heappush(current_intervals, first_start)
    overlaps = 0

    for start, end in intervals[1:]:
        if current_intervals:
            if current_intervals[0] < start:
                heapq.heappop(current_intervals)
                overlaps += len(current_intervals)
    return overlaps


def max_concurrency_attempt_5(points):
    """
    If len of intervals is 0 or 1 return immediately. Passes 2 tests.
    """
    if len(points) in [0, 1]:
        return len(points)

    """
    Push all intervals to heap
    """
    q = []
    for point in points:
        heapq.heappush(q, (point[0], point[1]))

    """
    Start with the top element in the heap
    """
    cur = heapq.heappop(q)
    cur_max = cur[1]
    res = []

    while q:
        point = heapq.heappop(q)

        """
        check if the last seen max falls in the new point interval. If it is then change the last seen max
        """
        if point[0] <= cur_max:
            cur_max = min(cur_max, point[1])

        else:
            """
            In this case last seen max doesn't fall in the new point interval. Push last seen max to ans and then res assign to new point end
            """
            res.append(cur_max)
            cur_max = point[1]
    res.append(cur_max)
    return len(res)


def max_concurrency(s):
    concurrent_jobs = 0
    max_jobs = 0
    heap = []
    if s:
        for start, end in s:
            heapq.heappush(heap, end)
            while heap[0] <= start:
                heapq.heappop(heap)
                concurrent_jobs -= 1
            concurrent_jobs += 1
            if concurrent_jobs > max_jobs:
                max_jobs = concurrent_jobs
    return max_jobs


def max_concurrency_attempt_7(self, trips: List[List[int]], capacity: int) -> bool:
    """Does not compile."""
    start = defaultdict(int)
    end = defaultdict(int)
    for trip in trips:
        start[trip[1]] += trip[0]
        end[trip[2]] += trip[0]
    curr = 0
    heapStart = []
    for key, value in start.items():
        heapq.heappush(heapStart, (key, value))
    heapEnd = []
    for key, value in end.items():
        heapq.heappush(heapEnd, (key, value))
    while heapStart:
        if heapEnd[0][0] <= heapStart[0][0]:
            curr -= heapq.heappop(heapEnd)[1]
        else:
            if heapStart[0][1] + curr > capacity:
                return False
            curr += heapq.heappop(heapStart)[1]
    return True


def max_concurrency_attempt_8(s):
    """Passes 4 tests."""
    intervalPoints = []
    for interval in s:
        heapq.heappush(intervalPoints, (interval[0], -1))
        heapq.heappush(intervalPoints, (interval[1], 1))
    maxOverlap = 0
    maxOverlapLocation = 0
    overlaps = 0
    while intervalPoints:
        index, val = heapq.heappop(intervalPoints)
        overlaps -= val
        if overlaps > maxOverlap:
            maxOverlap = overlaps
            maxOverlapLocation = index
    return maxOverlapLocation


def max_concurrency_pre_attempt_9(s):
    """Passes 7 tests."""
    s.sort(key=lambda x: x[1])
    f = 0
    heap = []
    for start, end in s:
        heapq.heappush(heap, -start)
        f += start
        if f >= end:
            f += heapq.heappop(heap)
    return len(heap)


def max_concurrency_attempt_9(s):
    pq = []
    start = 0
    for start_end in sorted(s, key=lambda x: x[1]):
        st, end = start_end[0], start_end[1]
        start += st
        heapq.heappush(pq, -st)
        while start >= end:
            start += heapq.heappop(pq)
    return len(pq)


def max_concurrency_attempt_10(s):
    """Fails all tests."""
    starts, ends = zip(*s)
    overlap = range(max(starts), min(ends) + 1)
    if not overlap:
        return ([], range(min(starts), max(ends) + 1), [])

    less_non_overlap = range(*heapq.nsmallest(2, starts))
    end, start = heapq.nlargest(2, ends)
    greater_non_overlap = range(start + 1, end + 1)
    return (overlap, less_non_overlap, greater_non_overlap)


def max_concurrency_attempt_11(s):
    """Fails all tests."""
    meetings = sorted(s, key=lambda k: k[1])

    heap = [(meetings[0][1], 0)]

    overlaps = {}

    for i in range(1, len(meetings)):
        if meetings[i][0] == heap[0][0]:
            heapq.heappush(heap, (meetings[i][1], i))
        else:
            heapq.heappop(heap)
            heapq.heappush(heap, (meetings[i][1], i))

        if meetings[i][0] <= heap[0][0]:
            p = (meetings[i][0], heap[0][0])
            if p in overlaps:
                overlaps[p] = max(overlaps[p], len(heap))
            else:
                overlaps[p] = len(heap)

    return [x for x, y in overlaps.items() if y == max(overlaps.values())]


# print(max_concurrency(start_and_end_times))
# start_time, end_time = start_and_end_time[0], start_and_end_time[1]
# overlap = min(end_time)
