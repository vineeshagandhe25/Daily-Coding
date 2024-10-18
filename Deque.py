# Double ended queues without using libraries
class Deque:
    def __init__(self):
        self.deque = []

    def add_front(self, item):
        self.deque.insert(0, item)

    def add_rear(self, item):
        self.deque.append(item)

    def remove_front(self):
        if not self.is_empty():
            return self.deque.pop(0)
        return "Deque is empty"

    def remove_rear(self):
        if not self.is_empty():
            return self.deque.pop()
        return "Deque is empty"

    def is_empty(self):
        return len(self.deque) == 0

# Example usage
dq = Deque()
dq.add_front(10)
dq.add_rear(20)
print(dq.remove_front())  # 10
print(dq.remove_rear())   # 20