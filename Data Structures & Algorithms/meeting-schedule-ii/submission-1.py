"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        starts = sorted(inter.start for inter in intervals)
        ends = sorted(inter.end for inter in intervals)

        s = 0
        e = 0

        current_rooms = 0
        max_rooms = 0

        while s < len(intervals):
            if starts[s] < ends[e]:
                current_rooms += 1
                max_rooms = max(max_rooms, current_rooms)
                s += 1

            else:
                current_rooms -= 1
                e += 1

        return max_rooms