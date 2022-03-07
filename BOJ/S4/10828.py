import sys

def push(X):
    stack.append(X)

def pop():
    global stack
    if stack == []:
        return -1
    else:
        a = stack[-1]
        stack = stack[:-1]
        return a

def size(stack):
    return len(stack)

def empty(stack):
    if stack == []:
        return 1
    else:
        return 0

def top(stack):
    if stack == []:
        return -1
    else:
        return stack[-1]

stack = []
N = int(sys.stdin.readline())
for _ in range(N):
    S = sys.stdin.readline().split()
    if S[0] == 'push':
        push(int(S[1]))
    elif S[0] == 'pop':
        print(pop())
    elif S[0] == 'size':
        print(size(stack))
    elif S[0] == 'empty':
        print(empty(stack))
    elif S[0] == 'top':
        print(top(stack))