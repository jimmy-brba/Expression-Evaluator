class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None

    def isEmpty(self):
        return self.top is None

    def push(self,data):
        node = Node(data)
        node.next=self.top
        self.top=node

    def pop(self):
        if(self.top is not None):
            node=self.top
            self.top=node.next
            val=node.data
            node=None
            return val

        return "Stack Underflow"

    def getTop(self):
        return self.top.data
  