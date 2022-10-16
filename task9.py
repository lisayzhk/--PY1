salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

grow = increase + 1
need_money = 0  # количество денег, чтобы прожить 10 месяцев
for money in range(1, months +1):
    money = spend - salary
    spend = spend * grow
    need_money += money


print(round(need_money))
