class Stack:
    
    def __init__(self):
        self.list_stack = []
        

    
    def push(self, item):
        self.list_stack.append(item)
        


    def pop(self):
        return self.list_stack.pop()


    def peek(self):
        return self.list_stack[-1]


    def size(self):
        return len(self.list_stack)


    def is_empty(self):
        return (self.list_stack == [])


def check(string):
    brackets_open = ('(', '[', '{')
    brackets_closed = (')', ']', '}')
    stack = Stack()
    for i in string:
        if i in brackets_open:
            stack.push(i)
        if i in brackets_closed:    
            if stack.size()  == 0:
                return False
            index = brackets_closed.index(i)
            open_bracket = brackets_open[index]
            if stack.peek() == open_bracket:
                stack.pop()
    return  stack.is_empty()


strings = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]']


for s in strings:
    if check(s):
        print('Сбалансирована')
    else:
        print(' Несбалансирована')
    

