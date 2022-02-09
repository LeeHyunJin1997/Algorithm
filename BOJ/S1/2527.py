def dots(x, y, p, q):
    dots_list = []

    for i in range(x, p+1):
        for j in range(y, q+1):
            dots_list.append((i, j))
    
    return dots_list

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    meeted_dots = list(set(dots(x1, y1, p1, q1)) & set(dots(x2, y2, p2, q2)))
    x_line = True
    y_line = True

    for i in range(len(meeted_dots)-1):
        if meeted_dots[i][0] != meeted_dots[i+1][0]:
            x_line = False

    for i in range(len(meeted_dots)-1):
        if meeted_dots[i][1] != meeted_dots[i+1][1]:
            y_line = False

    if len(meeted_dots) == 0:
        print('d')
    elif len(meeted_dots) == 1:
        print('c')
    elif x_line or y_line:
        print('b')
    else:
        print('a')