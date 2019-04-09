class Observation:
    first_value = 0
    temperature = 0

    def __init__(self, time, value):
        self.time = time
        self.value = value

    def __index__(self):
        return self.value

    def __iter__(self):
        return self
