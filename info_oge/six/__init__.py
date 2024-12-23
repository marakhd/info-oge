from typing import List


class NumSix:
    @staticmethod
    def evaluate_test_cases(conditions, test_cases: List[tuple]) -> list:
        """
        Функция для проверки условий и подсчета числа выполнений заданного условия.

        :param conditions: lambda-функция с условиями проверки
        :param test_cases: список тестовых случаев [(s1, t1), (s2, t2), ...]
        :return: количество случаев, при которых условия выполняются
        """
        yes_c = 0
        no_c = 0
        for case in test_cases:
            if conditions(*case):
                yes_c += 1
            else:
                no_c += 1
        print(f"ДА: {yes_c}, НЕТ: {no_c}")
        return yes_c, no_c


