'''
1 traverse a linked list
2 add to linked list (need something to check the array is not full)
3 delete from linked list
4 Extension1 - keeping track of space
5 Extension2 - produce a simple menu system for your linked list array approach

add comments
refactor your code to make it more maintainable - i.e. functions / procedures
'''

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


