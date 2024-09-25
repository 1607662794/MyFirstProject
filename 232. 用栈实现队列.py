class MyQueue:

    def __init__(self):
        self.stack_1 = []#顺序
        self.stack_2 = []#逆序

    def push(self, x: int) -> None:
        self.stack_1.append(x)

    def pop(self) -> int:
        self.peek()
        return self.stack_2.pop()

    def peek(self) -> int:
        if self.stack_2:
            return self.stack_2[-1]
        elif not self.stack_2 and self.stack_1:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
            return self.stack_2[-1]

    def empty(self) -> bool:
        if self.stack_1 or self.stack_2:
            return False
        return True


myQueue = MyQueue()
myQueue.push(1)
myQueue.pop()
myQueue.empty()