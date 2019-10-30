def fibonacci(number):
    if number in (1, 2):
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(11))

# Последовательность до 10:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

# Последовательность до 11:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
