# create node class
class Node():
    def __init__(self, newName):
        self.name = newName
        # next pointer will always point to none when created
        self.next = None
    
class LinkedList():
    def __init__(self, headData):
        self.head = Node(headData)
    
    def add(self, nodeData):
        # create new node
        newNode = Node(nodeData)
        # check if list is empty, if it is newNode becomes the headNode
        if self.head is None: 
            self.head = Node(nodeData)
        else:  
            # go through each pointer after the head, until the rear of the list is reached by a null pointer
            currentNode = self.head
            while (currentNode.next != None):
                currentNode = currentNode.next
            # make the next pointer for the last node the new node            
            currentNode.next = newNode
            
people = LinkedList("Lloyd")
people.add("Sarah")
people.add("Richard")
people.add("Claire")
people.add("Roberto")

print(people.head.next.name)
print(people.head.next.next.name)
print(people.head.next.next.next.name)
print(people.head.next.next.next.next.name)
print(people.head.next.next.next.next.next)


