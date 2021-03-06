

# Рекурсия по правилу если `Если 0 прекратить рекурсию`:
def recursion(depth=2) -> print:
    if depth != 0:
        # Если не 0 вызываем эту функцию ещё раз:
        print(f'Итераций осталось: {depth}')
        # Отнимаем 1 от depth что бы рекурсия не была бесконечной:
        recursion(depth=depth - 1)
    # Если ноль:
    else:
        print('Итераций не осталось :)')


# Рекурсия по невозможному правилу т.к. мы прибавляем 1, а не отнимаем.
# Упадёт с ошибкой RecursionError:
def infinity_recursion(depth=2) -> print:
    if depth != 0:
        # Если не 0 вызываем эту функцию ещё раз:
        print(f'Итераций осталось1: {depth}')
        # Прибавляем 1 к depth что бы рекурсия была
        # бесконечной и не выполнился else:
        infinity_recursion(depth=depth + 1)
    # Если ноль:
    else:
        print('Итераций не осталось :)')


# recursion(2)

infinity_recursion(995)

# try:
#     infinity_recursion(10)
# except RecursionError:
#     print('Рекурсия бесконечна!')
