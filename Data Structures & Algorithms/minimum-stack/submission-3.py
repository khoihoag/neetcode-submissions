class MinStack:

    def __init__(self):
        self.stack = []
        self.res = []
        self.pref_min = float("inf");

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.pref_min = min(self.pref_min, val)
        self.res.append(self.pref_min)

    def pop(self) -> None:
        self.stack.pop()
        self.res.pop()
        if self.res:
            self.pref_min = self.res[-1]
        else:
            self.pref_min = float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.res[-1]
