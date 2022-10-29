class Solution:
    def merge(self, intervals):
        intervals.sort(key = lambda x:x[0])
        answer = []
        last_left = intervals[0][0]
        last_right = intervals[0][1]
        if len(intervals) == 1:
            return [[last_left, last_right]]
        else:
            for i in range(1, len(intervals)):
                if intervals[i][0] <= last_right:
                    if intervals[i][1] > last_right:
                        last_right = intervals[i][1]
                else:
                    answer.append([last_left, last_right])
                    last_left = intervals[i][0]
                    last_right = intervals[i][1]
            if len(answer) == 0:
                answer.append([last_left, last_right])
            elif answer[-1][1] != last_right:
                answer.append([last_left, last_right])
            return answer

sol = Solution()
print(sol.merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
