head = 0
data = 0
pointer =1

linkedList = [
    ["Bob", 3],
    ["Sarah", 2],
    ["Sharon", None],
    ["Roberto", 1],
    [None, None],
    [None, None]
]

#check if list is empty
if (linkedList[head] == None):
    print("List Empty")
else:
    current = head
    while current != None:
        # start at the head
        print(linkedList[current][data])
        current = linkedList[current][pointer]
    
    # if the head is none, list is empty

# print data of current node
# go to the pointer of the current node
# if the pointer of the current node is none, then the list finished so stop


# print(linkedList[head][pointer])
# print(linkedList[linkedList[head][pointer]][pointer])


