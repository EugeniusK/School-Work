#############################################################################
# Stack class implemented with an array
class Stack:
    # Constructor
    def __init__(self):
        self.StackPointer = -1
        self.Max = 4
        self.Contents = ["" for Elements in range(self.Max)]

    # Add an item to the stack
    def Push(self, Item):
        if self.Max > self.StackPointer:
            self.StackPointer += 1
            self.Contents[self.StackPointer] = Item
        else:
            raise IndexError('OVERFLOW OVERFLOW OVERFLOW')

    # Remove an item from the stack
    def Pop(self):
        if self.StackPointer >= 0:
            self.Contents[self.StackPointer] = ""
            self.StackPointer -= 1
        else:
            raise IndexError('UNDERFLOW UNDERFLOW UNDERFLOW')
    # Look at the top item in the stack without removing it      
    def Peek(self):
        return self.Contents[self.StackPointer]

#############################################################################
# Main program starts here

# Subroutine to output the contents of a stack
def ClearStack(InputStack):
    Item = InputStack.Peek()
    while Item:
        Item = InputStack.Pop()
        if Item:
            print(Item)

# How to create a new stack
MyStack = Stack()

#How to push to the stack (returns True on success or False on stack overflow)
Action = MyStack.Push("Craig")
Action = MyStack.Push("Dave")
MyStack.Pop()
MyStack.Pop()
MyStack.Pop()
print(MyStack.Contents)
# How to pop from the stack (stack underflow returns None)
Item = MyStack.Pop()