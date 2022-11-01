class MyQueue:
    def __init__(self):
        self.right_order = []
        self.reverse_order = []

    def push(self, x: int) -> None:
        self.right_order.append(x)
        
    def pop(self) -> int:
        self.peek()
        return self.reverse_order.pop()

    def peek(self) -> int:
        if len(self.reverse_order) == 0:
            while len(self.right_order) != 0:
                self.reverse_order.append(self.right_order.pop())
        return self.reverse_order[-1]

    def empty(self) -> bool:
        return not self.right_order and not self.reverse_order


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
