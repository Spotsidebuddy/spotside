"""Сложение без переноса разряда"""

n1 = f"{input():0>4}"
n2 = f"{input():0>4}"

result = ""

for i in range(len(n1)):
    d1 = int(n1[i])
    d2 = int(n2[i])
    digit = (d1 + d2) % 10
    result += str(digit)

print(int(result))

# при форматировании после двоеточия не должен стоять пробел