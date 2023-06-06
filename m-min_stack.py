class MinStack:
    def __init__(self):
        self.l = deque()  # list of elements
        self.min = None  # current min
        self.mins = []  # increasing order of recent minimums

    def push(self, val: int) -> None:
        self.l.append(val)

        if self.min is None:
            self.min = val
            self.mins.append(self.min)
        elif self.min >= val:
            self.min = val
            self.mins.append(self.min)

    def pop(self) -> None:
        if self.l[-1] == self.mins[-1]:
            self.mins.pop(-1)

            if len(self.mins) != 0:
                self.min = self.mins[-1]
            else:
                self.min = None

        self.l.pop()

    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
