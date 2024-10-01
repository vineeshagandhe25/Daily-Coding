# For LIFO behavior (stack-like) you can use queue.LifoQueue.
import queue

# Create a LIFO queue
lifo_queue = queue.LifoQueue()

# Add elements to the queue
lifo_queue.put(10)
lifo_queue.put(20)
lifo_queue.put(30)

# Accessing and removing elements (LIFO)
while not lifo_queue.empty():
    print(lifo_queue.get())

# Time Complexity --- O(n) where n is no of input elements .
# Space Complexity --- O(n) where n is no of input elements .