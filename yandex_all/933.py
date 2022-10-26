from collections import deque
class RecentCounter:

    def __init__(self):
        self.array_ping = deque()
        

    def ping(self, t: int) -> int:
        self.array_ping.append(t)
        
        while self.array_ping[0] < (t - 3000):
            self.array_ping.popleft()
        return len(self.array_ping)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
