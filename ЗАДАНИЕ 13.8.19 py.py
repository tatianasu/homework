amount = 0
tickets = int(input('Пожалуйста, введите количество билетов '))
for i in range(tickets):
    age = int(input('Пожалуйста, введите возраст '))
    if age < 18:
        amount += 0
    elif 18 <= age <= 25:
        amount += 990
    else:
        amount += 1390
if tickets >= 3:
    amount = amount - amount/ 100 * 10

print("Итого: ", amount, "руб.")