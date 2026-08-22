import unittest
from typing import Any, Dict
from enforce_rules import validate


class TestValidate(unittest.TestCase):

    # -----------------------------
    # LENGTH RULES
    # -----------------------------
    def test_length_valid(self):
        self.assertEqual(validate([1, 2, 3], {"length": 3}), [1, 2, 3])

    def test_length_invalid(self):
        with self.assertRaises(ValueError):
            validate([1, 2], {"length": 3})

    def test_min_length_valid(self):
        self.assertEqual(validate([1, 2, 3], {"min_length": 2}), [1, 2, 3])

    def test_min_length_invalid(self):
        with self.assertRaises(ValueError):
            validate([1], {"min_length": 2})

    def test_max_length_valid(self):
        self.assertEqual(validate([1, 2], {"max_length": 3}), [1, 2])

    def test_max_length_invalid(self):
        with self.assertRaises(ValueError):
            validate([1, 2, 3, 4], {"max_length": 3})

    # -----------------------------
    # MIN / MAX
    # -----------------------------
    def test_min_valid(self):
        self.assertEqual(validate(5, {"min": 3}), 5)

    def test_min_invalid(self):
        with self.assertRaises(ValueError):
            validate(2, {"min": 3})

    def test_max_valid(self):
        self.assertEqual(validate(5, {"max": 10}), 5)

    def test_max_invalid(self):
        with self.assertRaises(ValueError):
            validate(20, {"max": 10})

    # -----------------------------
    # ALLOWED VALUES
    # -----------------------------
    def test_allowed_values_valid(self):
        self.assertEqual(validate("b", {"allowed_values": ("a", "b", "c")}), "b")

    def test_allowed_values_invalid(self):
        with self.assertRaises(ValueError):
            validate("x", {"allowed_values": ("a", "b", "c")})

    # -----------------------------
    # INVARIANT
    # -----------------------------
    def test_invariant_valid(self):
        self.assertTrue(validate(True, {"invariant": True}))

    def test_invariant_invalid(self):
        with self.assertRaises(ValueError):
            validate(False, {"invariant": True})

    # -----------------------------
    # ALL SAME / ALL UNIQUE
    # -----------------------------
    def test_all_same_valid(self):
        self.assertEqual(validate([1, 1, 1], {"all_same": True}), [1, 1, 1])

    def test_all_same_invalid(self):
        with self.assertRaises(ValueError):
            validate([1, 2, 1], {"all_same": True})

    def test_all_unique_valid(self):
        self.assertEqual(validate([1, 2, 3], {"all_unique": True}), [1, 2, 3])

    def test_all_unique_invalid(self):
        with self.assertRaises(ValueError):
            validate([1, 2, 2], {"all_unique": True})

    # -----------------------------
    # NON EMPTY / NO NULLS
    # -----------------------------
    def test_non_empty_valid(self):
        self.assertEqual(validate([1], {"non_empty": True}), [1])

    def test_non_empty_invalid(self):
        with self.assertRaises(ValueError):
            validate([], {"non_empty": True})

    def test_no_nulls_valid(self):
        self.assertEqual(validate([1, 2, 3], {"no_nulls": True}), [1, 2, 3])

    def test_no_nulls_invalid(self):
        with self.assertRaises(ValueError):
            validate([1, None, 3], {"no_nulls": True})

    # -----------------------------
    # SORTED / INCREASING / DECREASING
    # -----------------------------
    def test_sorted_valid(self):
        self.assertEqual(validate([1, 2, 3], {"sorted": True}), [1, 2, 3])

    def test_sorted_reverse_valid(self):
        self.assertEqual(validate([3, 2, 1], {"sorted": True}), [3, 2, 1])

    def test_sorted_invalid(self):
        with self.assertRaises(ValueError):
            validate([1, 3, 2], {"sorted": True})

    def test_increasing_valid(self):
        self.assertEqual(validate([1, 2, 3], {"increasing": True}), [1, 2, 3])

    def test_increasing_invalid(self):
        with self.assertRaises(ValueError):
            validate([1, 3, 2], {"increasing": True})

    def test_decreasing_valid(self):
        self.assertEqual(validate([3, 2, 1], {"decreasing": True}), [3, 2, 1])

    def test_decreasing_invalid(self):
        with self.assertRaises(ValueError):
            validate([3, 1, 2], {"decreasing": True})

    # -----------------------------
    # SUM MIN / SUM MAX
    # -----------------------------
    def test_sum_min_valid(self):
        self.assertEqual(validate([10, 20, 30], {"sum_min": 50}), [10, 20, 30])

    def test_sum_min_invalid(self):
        with self.assertRaises(ValueError):
            validate([10, 20], {"sum_min": 50})

    def test_sum_max_valid(self):
        self.assertEqual(validate([10, 20, 30], {"sum_max": 70}), [10, 20, 30])

    def test_sum_max_invalid(self):
        with self.assertRaises(ValueError):
            validate([50, 50], {"sum_max": 70})

    # -----------------------------
    # ELEMENT MIN / ELEMENT MAX
    # -----------------------------
    def test_element_min_valid(self):
        self.assertEqual(validate([10, 20, 30], {"element_min": 5}), [10, 20, 30])

    def test_element_min_invalid(self):
        with self.assertRaises(ValueError):
            validate([1, 20, 30], {"element_min": 5})

    def test_element_max_valid(self):
        self.assertEqual(validate([10, 20, 30], {"element_max": 40}), [10, 20, 30])

    def test_element_max_invalid(self):
        with self.assertRaises(ValueError):
            validate([10, 20, 100], {"element_max": 40})

    # -----------------------------
    # REGEX
    # -----------------------------
    def test_regex_valid(self):
        self.assertEqual(validate("cat", {"regex": "cat|dog"}), "cat")

    def test_regex_invalid(self):
        with self.assertRaises(ValueError):
            validate("bird", {"regex": "cat|dog"})

    # -----------------------------
    # MUST BE TRUE
    # -----------------------------
    def test_must_be_true_valid(self):
        def is_even(x: int) -> bool:
            return x % 2 == 0
        self.assertEqual(validate(8, {"must_be_true": is_even}), 8)

    def test_must_be_true_invalid(self):
        def is_even(x: int) -> bool:
            return x % 2 == 0
        with self.assertRaises(ValueError):
            validate(7, {"must_be_true": is_even})


if __name__ == "__main__":
    unittest.main()
