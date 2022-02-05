from sys import stdin

line_1 = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=']
line_2 = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\']
line_3 = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '\'']
line_4 = ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']

while True:
    gyo = stdin.readline().rstrip()

    if gyo == '':
        break

    rlt = ''

    for i in gyo:
        if i == ' ':
            rlt += ' '
        elif i in line_1:
            rlt += line_1[line_1.index(i)-1]
        elif i in line_2:
            rlt += line_2[line_2.index(i)-1]
        elif i in line_3:
            rlt += line_3[line_3.index(i)-1]
        elif i in line_4:
            rlt += line_4[line_4.index(i)-1]
        
    print(rlt)