from collections import deque
stack = deque()

s = []
s.append('https://www.cnn.com/')
s.append('https://www.cnn.com/world')
s.append('https://www.cnn.com/india')
s.append('https://www.cnn.com/china')

s.pop()
print(s[-1])

print(dir(stack))

stack.append("https://www.cnn.com/")
stack.append("https://www.cnn.com/world")
stack.append("https://www.cnn.com/india")
stack.append("https://www.cnn.com/china")
print(stack)

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
s = Stack()
s.push(5)
s.push(9)
s.push(34)
s.push(78)
s.push(12)
s.is_empty()
s.pop()
print(s.container)