class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        answer = []
        i, j = 0, 0
        while (i < len(firstList)) and (j < len(secondList)):
            lb = max(firstList[i][0], secondList[j][0])
            rb = min(firstList[i][1], secondList[j][1])
            
            if lb <= rb:
                answer.append([lb, rb])
            
            if firstList[i][1] > secondList[j][1]:
                j += 1
            else:
                i += 1
        return answer
