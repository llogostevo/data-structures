queue = []

# enqueue
def enqueue(personName):
    # add to the rear of the queue
    queue.append(personName)

enqueue("bob")
enqueue("ricardo")
enqueue("saskia")
enqueue("ulrika")

print(queue)
print(queue)

def dequeue():
    return queue.pop(0)


print(dequeue())
print(queue)
