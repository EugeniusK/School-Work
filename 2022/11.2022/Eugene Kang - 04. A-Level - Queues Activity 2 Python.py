#############################################################################
# Queue class implemented with an array
class Queue:
    # Constructor
    def __init__(self):
        self.FrontPointer = 0
        self.BackPointer = -1
        self.Max = 4
        self.Contents = ["" for Elements in range(self.Max)]

    # Add an item to the queue
    def Enqueue(self, Item):
        if self.Contents[(self.BackPointer + 1) % self.Max] == '':
            self.BackPointer = (self.BackPointer + 1) % self.Max
            self.Contents[self.BackPointer] = Item
        else:
            return False

    # Remove an item from the queue
    def Dequeue(self):
        output = self.Contents[self.FrontPointer]

        if output == '':
            return None
        else:
            self.Contents[self.FrontPointer] = ''
            self.FrontPointer = (self.FrontPointer + 1) % self.Max

            return output
    # Look at the next item in the queue without removing it      
    def Peek(self):
        if self.Contents[self.FrontPointer] != '':
            return self.Contents[self.FrontPointer]
        else:
            return None
#############################################################################
# Main program starts here

# Subroutine to output the contents of a queue
def ClearQueue(InputQueue):
    Item = InputQueue.Peek()
    while Item:
        Item = InputQueue.Dequeue()
        if Item:
            print(Item)

# How to create a new queue (you can have as many queue objects as you want using lists)
MyQueue = Queue()

#How to add to the queue (returns True on success or False on queue overflow)
Action = MyQueue.Enqueue("Craig")
Action = MyQueue.Enqueue("Dave")
# How to remove from the queue (queue underflow returns None)
Item = MyQueue.Dequeue()
# Output the entire stack using the ClearQueue subroutine
ClearQueue(MyQueue)