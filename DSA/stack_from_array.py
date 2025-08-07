class Stack:
    def __init__(self, cap) -> None:
        self.cap = cap
        self.top = -1
        self.a = [0]*cap

    def push(self, n):
        if self.top>=self.cap-1:
            print("Stack is full")
            return False
        self.top += 1
        self.a[self.top] = n
        return True

    def pop(self):
        if self.top < 0:
            print("Stack is empty")
            return False

        popped = self.a[self.top]
        self.top -= 1
        return popped

    def peek(self):
        if self.top < 0:
            print("Stack is Empty")
            return False
        return self.a[self.top]

    def isEmpty(self):
        if self.top<0:
            return True
        return False


        

        
