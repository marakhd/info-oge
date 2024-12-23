from info_oge.five import NumFive

# Команды "прибавь 5" и "умножь на b"
commands_alpha = {
    1: (lambda x, y: x + y, 5),  # Добавить 5
    2: (lambda x, y: x * y, None),  # Умножить на b
}

start = 3
end = 88
program = "11211"
NumFive.find_b(start, end, program, commands_alpha, b_min=2, b_max=88)

#or

# Пример: вычти 3 и умножь на 5
commands_calculator = {
    1: (lambda x, y: x - y, 3),  # Вычесть 3
    2: (lambda x, y: x * y, 5),  # Умножить на 5
}

start = 3
end = 42
program = NumFive.find_program(start, end, commands_calculator, max_length=5)
