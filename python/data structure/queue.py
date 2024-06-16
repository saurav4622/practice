queue = [1, 2, 3, 4, 5, 6]
print("Original queue: ", queue)
queue.append(7)
print("Queue after insertion is: ", queue)
queue.pop(0)
print("Queue after deletion is: ", queue)
print("value obtained after pop operation is: ", queue[len(queue) - 1])
