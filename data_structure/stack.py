size = 3
data = [2]*size

top = -1

def push(x):
    global top
    if top>=size-1:
        print("Stack Overflow")
    else:
        top+=1
        data[top]=x
        print(x)

for i in range(4):
    push(i)