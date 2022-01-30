# 일곱 난쟁이 키의 합은 100
import random
height = []
real = []

for i in range(9):
    height.append(int(input()))

while sum(real) != 100:
    real = random.sample(height, 7)

for i in range(len(real)):
    print(min(real))
    real.remove(min(real))