class NumFive:
    def __execute_program(start, program, commands, b=None):
        """
        Выполняет программу и возвращает результат.

        :param start: начальное число
        :param program: последовательность команд
        :param commands: словарь команд вида {номер: (функция, аргумент)}
        :param b: неизвестный параметр, используется при необходимости
        :return: результат выполнения программы
        """
        current = start
        for cmd in program:
            if cmd == "1":  # Первая команда
                func, arg = commands[1]
                current = func(current, arg)
            elif cmd == "2":  # Вторая команда
                func, arg = commands[2]
                current = func(current, arg if b is None else b)
        return current

    @classmethod
    def find_b(cls, start, end, program, commands, b_min=2, b_max=10):
        """
        Находит значение b, при котором программа переводит start в end.

        :param start: начальное число
        :param end: конечное число
        :param program: последовательность команд
        :param commands: словарь команд вида {номер: (функция, аргумент)}
        :param b_min: минимальное значение b
        :param b_max: максимальное значение b
        :return: найденное значение b или None
        """
        for b in range(b_min, b_max + 1):
            if cls.__execute_program(start, program, commands, b=b) == end:
                print("Найденное значение b:", b)
                return b

    @classmethod
    def find_program(cls, start, end, commands, max_length):
        """
        Находит последовательность команд, переводящую start в end.

        :param start: начальное число
        :param end: конечное число
        :param commands: словарь команд вида {номер: (функция, аргумент)}
        :param max_length: максимальная длина программы
        :return: программа или None
        """
        from itertools import product
        for length in range(1, max_length + 1):
            for program in product("12", repeat=length):  # Генерация всех программ
                if cls.__execute_program(start, ''.join(program), commands) == end:
                    print("Найдена программа:", ''.join(program))
                    return ''.join(program)
                
# Пример: вычти 3 и умножь на 5
commands_calculator = {
    1: (lambda x, y: x * y, 4),  # Вычесть 3
    2: (lambda x, y: x - y, 2),  # Умножить на 5
}

start = 3
end = 30
program = NumFive.find_program(start, end, commands_calculator, max_length=5)

