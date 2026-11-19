class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
            List of intervals where start is always less than end, assume they are sorted by start time

            return a list where overlapping is merged

            two pointer approach

            l, r pointers

            while l < len(list) - 1
                if overlapping merge them and remove them from the list
                else increment l and r both by 1
            
            return the list
        """

        l = 0
        r = 1

        intervals.sort(key=lambda x: x[0])

        while l < len(intervals) - 1:
            start_l, end_l = intervals[l]
            start_r, end_r = intervals[r]

            if start_r <= end_l:
                new = [min(start_l, start_r), max(end_l, end_r)]
                intervals[l] = new
                intervals.pop(r)
            else:
                l += 1
                r += 1
        return intervals
        