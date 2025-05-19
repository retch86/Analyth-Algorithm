import unittest
from distance import *
import json
import datetime
import io

class TestLevenshteinIterative(unittest.TestCase):
    def test_same_strings(self):
        self.assertEqual(iterative_levenstein_two_rows("таблица", "таблица"), 0)

    def test_empty_strings(self):
        self.assertEqual(iterative_levenstein_two_rows("", ""), 0)

    def test_complex(self):
        self.assertEqual(iterative_levenstein_two_rows("deepcopy", "раздел"), 8)

    def test_inversion(self):
        self.assertEqual(iterative_levenstein_two_rows("insert", "tresni"), 6)

    def test_two_adjacent_symbols(self):
        self.assertEqual(iterative_levenstein_two_rows("heart", "heatr"), 2)

    def test_single_char_difference(self):
        self.assertEqual(iterative_levenstein_two_rows("город", "горо"), 1)

    def test_single_char_difference(self):
        self.assertEqual(iterative_levenstein_two_rows("1234", "2143"), 3)
    

class TestLevenshteinRecursive(unittest.TestCase):
    def test_same_strings(self):
        self.assertEqual(recursive_levenstein("таблица", "таблица"), 0)

    def test_empty_strings(self):
        self.assertEqual(recursive_levenstein("", ""), 0)

    def test_complex(self):
        self.assertEqual(recursive_levenstein("deepcopy", "раздел"), 8)

    def test_inversion(self):
        self.assertEqual(recursive_levenstein("insert", "tresni"), 6)

    def test_two_adjacent_symbols(self):
        self.assertEqual(recursive_levenstein("heart", "heatr"), 2)

    def test_single_char_difference(self):
        self.assertEqual(recursive_levenstein("город", "горо"), 1)

    def test_single_char_difference(self):
        self.assertEqual(iterative_levenstein_two_rows("1234", "2143"), 3)

class TestLevenshteinRecursiveMatrix(unittest.TestCase):
    
    def test_same_strings(self):
        str_1 = "таблица"
        str_2 = "таблица"
        len_str_1 = len(str_1)
        len_str_2 = len(str_2)
        matrix = create_matrix(len_str_2 + 1, len_str_1 + 1)
        distance, matrix= recursive_levenstein_matrix(str_1, str_2, len_str_1, len_str_2, matrix)
        self.assertEqual(distance, 0)

    def test_empty_strings(self):
        str_1 = ""
        str_2 = ""
        len_str_1 = len(str_1)
        len_str_2 = len(str_2)
        matrix = create_matrix(len_str_2 + 1, len_str_1 + 1)
        distance, matrix = recursive_levenstein_matrix(str_1, str_2, len_str_1, len_str_2, matrix)
        self.assertEqual(distance, 0)

    def test_complex(self):
        str_1 = "deepcopy"
        str_2 = "раздел"
        len_str_1 = len(str_1)
        len_str_2 = len(str_2)
        matrix = create_matrix(len_str_2 + 1, len_str_1 + 1)
        distance, matrix= recursive_levenstein_matrix(str_1, str_2, len_str_1, len_str_2, matrix)
        self.assertEqual(distance, 8)

    def test_inversion(self):
        str_1 = "insert"
        str_2 = "tresni"
        len_str_1 = len(str_1)
        len_str_2 = len(str_2)
        matrix = create_matrix(len_str_2 + 1, len_str_1 + 1)
        distance, matrix = recursive_levenstein_matrix(str_1, str_2, len_str_1, len_str_2, matrix)
        self.assertEqual(distance, 6)

    def test_two_adjacent_symbols(self):
        str_1 = "heart"
        str_2 = "heatr"
        len_str_1 = len(str_1)
        len_str_2 = len(str_2)
        matrix = create_matrix(len_str_2 + 1, len_str_1 + 1)
        distance, matrix= recursive_levenstein_matrix(str_1, str_2, len_str_1, len_str_2, matrix)
        self.assertEqual(distance, 2)

    def test_single_char_difference(self):
        str_1 = "город"
        str_2 = "горо"
        len_str_1 = len(str_1)
        len_str_2 = len(str_2)
        matrix = create_matrix(len_str_2 + 1, len_str_1 + 1)
        distance, matrix = recursive_levenstein_matrix(str_1, str_2, len_str_1, len_str_2, matrix)
        self.assertEqual(distance, 1)

    def test_single_char_difference(self):
        str_1 = "1234"
        str_2 = "2143"
        len_str_1 = len(str_1)
        len_str_2 = len(str_2)
        matrix = create_matrix(len_str_2 + 1, len_str_1 + 1)
        distance, matrix = recursive_levenstein_matrix(str_1, str_2, len_str_1, len_str_2, matrix)
        self.assertEqual(distance, 2)

class TestDamerayLevenshteinRecursive(unittest.TestCase):
    def test_same_strings(self):
        self.assertEqual(recursive_dameray_levenstein("таблица", "таблица"), 0)

    def test_empty_strings(self):
        self.assertEqual(recursive_dameray_levenstein("", ""), 0)

    def test_complex(self):
        self.assertEqual(recursive_dameray_levenstein("deepcopy", "раздел"), 8)

    def test_inversion(self):
        self.assertEqual(recursive_dameray_levenstein("insert", "tresni"), 5)

    def test_two_adjacent_symbols(self):
        self.assertEqual(recursive_dameray_levenstein("heart", "heatr"), 1)

    def test_single_char_difference(self):
        self.assertEqual(recursive_dameray_levenstein("город", "горо"), 1)

    def test_single_char_difference(self):
        self.assertEqual(recursive_dameray_levenstein("1234", "2143"), 2)

if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_suite.addTests([
        unittest.TestLoader().loadTestsFromTestCase(TestLevenshteinIterative),
        unittest.TestLoader().loadTestsFromTestCase(TestLevenshteinRecursive),
        unittest.TestLoader().loadTestsFromTestCase(TestLevenshteinRecursiveMatrix),
        unittest.TestLoader().loadTestsFromTestCase(TestDamerayLevenshteinRecursive)
    ])

    test_runner = unittest.TextTestRunner(stream=io.StringIO(), resultclass=unittest.TextTestResult)
    test_result = test_runner.run(test_suite)

    total_tests = test_result.testsRun
    failed_tests = len(test_result.failures) + len(test_result.errors)
    passed_tests = total_tests - failed_tests
    coverage = 0.1

    timestamp = datetime.datetime.now().astimezone().isoformat()

    report_data = {
        "timestamp": timestamp,
        "coverage": coverage,
        "passed": passed_tests,
        "failed": failed_tests
    }

    with open("code/stud-unit-test-report-prev.json", "w") as report_file:
        json.dump(report_data, report_file, indent=4)