class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]
        left, right = 0, len(values) -1
        result = ""

        while left <= right:
            mid = (left + right) // 2
            
            mid_timestamp, value = values[mid]
            if timestamp >= mid_timestamp:
                result = value
                left = mid + 1

            else:
                right = mid - 1

        return result
