class Counter():
    instance = 0

    def __init__(self):
        Counter.instance += 1
        self.reset()

    def reset(self):
        self.value = 0

    def increment(self, amount=1):
        self.value += amount

    def decrement(self, amount=1):
        self.value -= amount

    def getValue(self):
        return self.value

    def __str__(self):
        return str(selv.value)

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) != type(other):
            return False
        return self.value == other.value
