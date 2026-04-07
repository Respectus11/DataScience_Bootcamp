"""
Simplified Unit Tests for StatEngine
"""

import unittest
import math
import sys
import os

# Setup path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from stat_engine import StatEngine


class TestStatEngine(unittest.TestCase):

    def setUp(self):
        self.basic = StatEngine([1, 2, 3, 4, 5])
        self.even = StatEngine([2, 4, 6, 8])
        self.sample = StatEngine([2, 4, 4, 4, 5, 5, 7, 9])

    # --- Mean / Median ---
    def test_mean(self):
        self.assertEqual(self.basic.get_mean(), 3.0)
        self.assertEqual(self.even.get_mean(), 5.0)

    def test_median(self):
        self.assertEqual(self.basic.get_median(), 3)
        self.assertEqual(self.even.get_median(), 5.0)

    # --- Mode ---
    def test_mode(self):
        self.assertEqual(StatEngine([1, 2, 2, 3]).get_mode(), [2])
        self.assertEqual(
            StatEngine([1, 2, 3]).get_mode(),
            "All values are unique - no mode exists"
        )

    # --- Variance / Std Dev ---
    def test_variance(self):
        self.assertAlmostEqual(self.sample.get_variance(False), 4.0)
        self.assertAlmostEqual(self.sample.get_variance(True), 32/7)

    def test_std_dev(self):
        self.assertAlmostEqual(self.sample.get_standard_deviation(False), 2.0)
        self.assertAlmostEqual(
            self.sample.get_standard_deviation(True),
            math.sqrt(32/7),
            places=5
        )

    # --- Outliers ---
    def test_outliers(self):
        data = StatEngine([1, 2, 3, 4, 5, 100])
        self.assertIn(100, data.get_outliers())

    # --- Summary ---
    def test_summary_keys(self):
        summary = self.basic.get_summary()
        keys = ['mean', 'median', 'mode', 'min', 'max']
        for k in keys:
            self.assertIn(k, summary)

    # --- Edge Cases ---
    def test_errors(self):
        with self.assertRaises(ValueError):
            StatEngine([])
        with self.assertRaises(TypeError):
            StatEngine([1, 'bad', 3])

    def test_single_value(self):
        s = StatEngine([42])
        self.assertEqual(s.get_mean(), 42.0)
        self.assertEqual(s.get_variance(False), 0.0)

    # --- Magic Methods ---
    def test_repr_len(self):
        self.assertIn('StatEngine', repr(self.basic))
        self.assertEqual(len(self.basic), 5)


if __name__ == "__main__":
    unittest.main()