q = ["", "", "", "", ""]
qSize = 0
front = -1
rear = 0

def isFull():
    global qSize
    if qSize == 5: 
        return True
    else: 
        return False
    
def isEmpty():
    global qSize
    if qSize == 0: 
        return True
    else: 
        return False
    
def enqueue(data):
    global rear, qSize, q
    # check if queueFull
    if isFull():
        print("Error: Queue Full")
    else: 
        q[rear]=data
        qSize +=1
        rear = (rear+1) % len(q)


def deQueue():
    global front, qSize, q
    if isEmpty():
        print("Error: Queue Empty")
    else: 
        value = q[front]
        front = (front+1) % len(q)
        qSize -=1
        return value


# TEST CASES
    
# Test Case 1: Enqueue elements
enqueue("A")
enqueue("B")
enqueue("C")
enqueue("D")
enqueue("E")

print(q)
print("Q Size: ", qSize)

# Test Case 2: Attempt to enqueue when the queue is full
enqueue("F")
print(q)
print("Q Size: ", qSize)


# Test Case 3: Dequeue elements
print(deQueue())  # Output should be "A"
print(deQueue())  # Output should be "B"
print(q)
print("Q Size: ", qSize)


# Test Case 4: Attempt to dequeue when the queue is empty
print(deQueue())  # Output should be "Error: Queue Empty"
print(q)
print("Q Size: ", qSize)


# Test Case 5: Enqueue after dequeue
enqueue("F")
enqueue("G")
print(q)
print("Q Size: ", qSize)


# Test Case 6: Attempt to enqueue when the queue is full
enqueue("H")  # Output should be "Error: Queue Full"

print(q)
print("Q Size: ", qSize)
