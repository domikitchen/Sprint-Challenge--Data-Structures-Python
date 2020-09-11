class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.count = 0

    def append(self, item):
        # if len(self.data) <= 5:
        #     self.data.append(item)
        # if len(self.data) >= 6:
        #     self.data.append(item)
        #     self.data.pop(0)
        if len(self.data) <= 5:
            self.data.append(item)
        if len(self.data) > 5:
            self.data[self.count] = item
            self.data.pop()
            if self.count >= 4:
                self.count = 0
            else:
                self.count += 1

    def get(self):
        return self.data