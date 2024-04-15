import random

def interpret(code):
    output = ""
    codeSplited = code.split('\n')
    grid = []
    lineLength = max((len(i) for i in codeSplited))
    direction = 'right'
    stringMode = False
    for line in codeSplited:
        row = []
        for char in line:
            row.append(char)
        while len(row) < lineLength:
            row.append(' ')
        grid.append(row)

    x = 0
    y = 0
    stack = []
    while grid[y][x] != '@':
        if stringMode and grid[y][x] != '"':
            stack.append(ord(grid[y][x]))
            y, x = move(y, x, direction, grid)
            continue
        elif grid[y][x].isdigit():
            stack.append(int(grid[y][x]))
        elif grid[y][x] == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b)
        elif grid[y][x] == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append(b-a)
        elif grid[y][x] == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(a*b)
        elif grid[y][x] == '/':
            a = stack.pop()
            b = stack.pop()
            if a == 0:
                stack.append(0)
            else:
                stack.append(b//a)
        elif grid[y][x] == '%':
            a = stack.pop()
            b = stack.pop()
            if a == 0:
                stack.append(0)
            else:
                stack.append(b%a)
        elif grid[y][x] == '!':
            value = stack.pop()
            if value == 0:
                stack.append(1)
            else:
                stack.append(0)
        elif grid[y][x] == '`':
            a = stack.pop()
            b = stack.pop()
            if b > a:
                stack.append(1)
            else:
                stack.append(0)
        elif grid[y][x] == '>':
            direction = 'right'
        elif grid[y][x] == '<':
            direction = 'left'
        elif grid[y][x] == '^':
            direction = 'up'
        elif grid[y][x] == 'v':
            direction = 'down'
        elif grid[y][x] == '?':
            direction = random.choice(['right', 'left', 'up', 'down'])
        elif grid[y][x] == '_':
            value = stack.pop()
            if value == 0:
                direction = 'right'
            else:
                direction = 'left'
        elif grid[y][x] == '|':
            value = stack.pop()
            if value == 0:
                direction = 'down'
            else:
                direction = 'up'
        elif grid[y][x] == '"':
            stringMode = not stringMode
        elif grid[y][x] == ':':
            if stack:
                stack.append(stack[-1])
            else:
                stack.append(0)
        elif grid[y][x] == '\\':
            if len(stack) == 1:
                value = stack.pop()
                stack.append(0)
                stack.append(value)
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(a)
                stack.append(b)
        elif grid[y][x] == '$':
            stack.pop()
        elif grid[y][x] == '.':
            output += str(stack.pop())
        elif grid[y][x] == ',':
            output += str(chr(stack.pop()))
        elif grid[y][x] == '#':
            y, x = move(y, x, direction, grid)
        elif grid[y][x] == 'p':
            y_ = stack.pop()
            x_ = stack.pop()
            v = stack.pop()
            grid[y_][x_] = chr(v)
        elif grid[y][x] == 'g':
            y_ = stack.pop()
            x_ = stack.pop()
            stack.append(ord(grid[y_][x_]))
        elif grid[y][x] == ' ':
            pass

        y, x = move(y, x, direction, grid)

    
    return output

def move(y, x, direction, grid):
    
    if direction == 'right':
        x += 1
    elif direction == 'left':
        x -= 1
    elif direction == 'up':
        y -= 1
    elif direction == 'down':
        y += 1

    if x < 0:
        x += len(grid[0])
    elif x == len(grid[0]):
        x = 0
    if y < 0:
        y += len(grid)
    elif y == len(grid):
        y = 0
    
    return y, x



#Sieve of Eratosthenes
code = '2>:3g" "-!v\\  g30          <\n\
 |!`"O":+1_:.:03p>03g+:"O"`|\n\
 @               ^  p3\" ":<\n\
2 234567890123456789012345678901234567890123456789012345678901234567890123456789'
print(interpret(code))
