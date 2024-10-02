# Interleave the First Half with Second Half:

'''Interleave the First Half of a Queue with the Second Half
Initial Queue: [1, 2, 3, 4, 5, 6, 7, 8]
Final Queue: [1, 5, 2, 6, 3, 7, 4, 8]'''

print("\nInterleave the First Half of a Queue with the Second Half")

def interleave_queue(q):
    size = len(q) // 2
    first_half = []

    # Dequeue the first half into a stack
    for _ in range(size):
        first_half.append(q.pop(0))

    # Interleave the queue with its first half
    while first_half:
        q.append(first_half.pop(0))  # Push front elements back
        q.append(q.pop(0))           # Push the next element from the original queue

queue = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"Initial Queue: {queue}")
interleave_queue(queue)
print(f"Final Queue: {queue}")

# Time Complexity --- O(n) where n is length of given queue.
# Space Complexity --- O(n) where n is length of given queue.