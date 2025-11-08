from collections import deque

class PlayQueue:
    def __init__(self):
        self._queue = deque()

    def add(self, item: str):
        self._queue.append(item)

    def next(self):
        return self._queue.popleft() if self._queue else None

    def clear(self):
        self._queue.clear()

    def peek_all(self):
        return list(self._queue)
