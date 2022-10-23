class Solution:
    def for_array(self, seats):
        first_i = 0
        while seats[first_i] != 1:
            first_i += 1
        
        max_seat = [0] * len(seats)
        counter = 0
        for i, elem in enumerate(seats):
            if elem == 0:
                counter += 1
            else:
                counter = 0
            max_seat[i] = counter
        return first_i, max_seat
            
    def maxDistToClosest(self, seats):
        first_i, max_seat = self.for_array(seats)
        seats_rev = [seats[i] for i in range(len(seats)-1, -1, -1)]
        first_i_rev, max_seat_rev = self.for_array(seats_rev)
        for i in range(len(max_seat)):
            first_n = max_seat[i]
            first_n_rev = max_seat_rev[len(max_seat) - i - 1]
            max_seat[i] = min(first_n, first_n_rev)
        return max(max(max_seat), first_i_rev, first_i)


sol = Solution()
print(sol.maxDistToClosest([0,1]))
