import unittest
from math_quiz import get_random_num, get_random_operation, operation


class TestMathGame(unittest.TestCase):

    def test_get_random_num(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_random_num(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def  test_get_random_operation(self):
        # TODO
        # test if it returns all of the set { +, - , *}
        for _ in range(1000):  # Test a large number of random values
            o = get_random_operation()
            self.assertTrue(o in ['+','-','*'])
        pass

    def test_operation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (3 , 1 , '-' ,'3 - 1',2),
                (5 , 1 , '*' ,'5 * 1',5),
                (0 , 0 , '-' ,'0 - 0',0),
                (0 , 5 , '*' ,'0 * 5',0)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                p,a = operation(num1,num2,operator)
                self.assertTrue(p==expected_problem)
                self.assertTrue(a==expected_answer)

                pass

if __name__ == "__main__":
    unittest.main()
