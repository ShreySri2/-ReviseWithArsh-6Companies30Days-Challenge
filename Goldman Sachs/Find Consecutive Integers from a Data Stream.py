class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = deque()
        self.value = value
        self.k = k
        self.consecutive_count = 0

    def consec(self, num: int) -> bool:
        self.stream.append(num)

        if num == self.value:
            self.consecutive_count += 1

        if len(self.stream) > self.k:
            removed_num = self.stream.popleft()
            if removed_num == self.value:
                self.consecutive_count -= 1

        return self.consecutive_count == self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)