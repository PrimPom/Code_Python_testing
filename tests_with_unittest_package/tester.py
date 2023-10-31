import unittest
from to_test.to_test import MathsOperations


class MathsOperationsTestCase(unittest.TestCase):

    def test_function_addition(self):
        """
        Fonction pour tester la fonction addition
        :return:
        """
        self.assertEqual(3, MathsOperations.addition(1, 2))
        self.assertEqual(1002, MathsOperations.addition(1000, 2))

    def test_function_soustraction(self):
        """
        Fonction pour tester la fonction de soustraction
        :return:
        """
        self.assertEqual(10, MathsOperations.soustraction(20, 10))
        self.assertEqual(190, MathsOperations.soustraction(200, 10))

    def test_function_multiplication(self):
        """
        Fonction pour tester la fonction de multiplication
        :return:
        """
        self.assertEqual(12, MathsOperations.multiplication(6, 2))

    def test_function_division(self):
        """
        Fonction pour tester la fonction de division
        :return:
        """
        self.assertEqual(3, MathsOperations.division_entiere(6, 2), msg="Division test 1")
        self.assertEqual(7, MathsOperations.division_entiere(49, 7), msg="Division test 2")


if __name__ == '__main__':
    unittest.main()
