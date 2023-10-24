class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def cycle_detection(head: Node) -> Node:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return fast


head = Node(50)
head.next = Node(40)
head.next.next = Node(30)
head.next.next.next = Node(20)
head.next.next.next.next = Node(10)

# adding a loop for the sake
# of this example
temp = head
while (temp.next != None):
    temp = temp.next
# loop added
temp.next = head

loopStart = cycle_detection(head)
if (loopStart == None):
    print("Loop does not exists")
else:
    print(f"Loop does exists and starts from {loopStart.value}")
