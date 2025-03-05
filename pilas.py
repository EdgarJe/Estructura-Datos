def create_stack():
    stack = []
    return stack


def check_empty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)
    print("pushed item: " + str(item))


def pop(stack):
    if check_empty(stack):
        return "stack is empty"
    return stack.pop()


stack = create_stack()
push(stack, "1")       
push(stack, "2")
push(stack, "3")
push(stack, "4")

print("popped item: " + pop(stack))
print("stack after popping an item: " + str(stack))