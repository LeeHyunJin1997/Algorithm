input_list = []

for i in range(4):
    input_list.append(int(input()))

x = sum(input_list)//60
y = sum(input_list)%60

print(x)
print(y)