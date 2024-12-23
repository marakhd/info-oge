from info_oge.four import NumSix

conditions = lambda s, t: s < 4 or t < 4
test_cases = [(3, 4), (5, 4), (-2, 1), (5, 6), (7, 8), (-5, 5), (-2, 2), (4, 3), (3, -8)]

print(NumSix.evaluate_test_cases(conditions, test_cases))