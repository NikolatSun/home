
1 уровень


x = int(input('Введите сумму вклада: '))
p = int(input('Введите процент: '))
y = int(input('Введите сумму цели: '))
i = 0
while x < y:
    x *= 1 + p / 100
    x = int(100 * x) / 100
    i += 1
print('Понадобится ', i)

2 Уровень

n = int(input('Число повторений: '))
i = 1
while i <= n:
    print(i)
    i += 1


3 Уровень

x = int(input())
summ = 0
while x > 0:
    summ += x % 10
    x //= 10
 
print(summ)
