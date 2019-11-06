# Массив (лист) неупорядоченных чисел:
massive = [10000, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -10000]

# Длинна массива:
N = len(massive)

# Итерируемся по длинне массива -1 т.к. последняя итерация будет лишней во
# внешнем цикле:
for i in range(N - 1):
    # Итерируемся по длинне масива - элемент внешней итерации - 1:
    for j in range(N - i - 1):
        # Если это число больше следующего число:
        if massive[j] > massive[j + 1]:
            # Меняем их местами:
            massive[j], massive[j + 1] = massive[j + 1], massive[j]

print(massive)