name = input()
price, weight, money = map(int, [input() for i in range(3)])

total = price * weight
change = money - total

pr_str = f'{weight}кг * {price}руб/кг'

s = 35

print(f"{'Чек':=^{s}}")
print(f"Товар:{name:>{(s - len('товар:'))}}")
print(f"Цена:{pr_str:>{(s - len('Цена:'))}}")
print(f"Итого:{total:>{(s - (len('Итого:') + len('руб')))}}руб")
print(f"Внесено:{money:>{(s - (len('Внесено:') + len('руб')))}}руб")
print(f"Сдача:{change:>{(s - (len('Сдача:') + len('руб')))}}руб")
print('=' * 35)