print("Програма запущана")
print("Введіть числа через пробіл які потрібно записати в список a")
a = [int(i) for i in input().split(' ')]
print("Введіть числа через пробіл які потрібно записати в список b")
b = [int(i) for i in input().split(' ')]
num = int(input("Введіть ціле число :\n"))
print("Результат : ", a + b if num < 0 else b + a)