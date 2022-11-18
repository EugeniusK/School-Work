#define a stack
class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
        
characters = input()
stack1 = Stack()
for c in range(0, len(characters)):
    stack1.push(characters[c])

stack2 = Stack()
for c in range(len(characters)-1, -1, -1):
    stack2.push(characters[c])

is_palindrome = True
for i in range(0, len(characters)):
    tmp_a = stack1.pop()
    tmp_b = stack2.pop()
    if tmp_a != tmp_b:
        is_palindrome = False
print(characters, is_palindrome)