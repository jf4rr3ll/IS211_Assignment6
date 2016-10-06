#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test functions"""

import decimal
import conversion
import unittest


class TestCases(unittest.TestCase):
    def test_fahrenheit_to_celsius(self):
        """Tests the Fahrenheit to celsius Conversion"""

        expected = ((decimal.Decimal(397) - 32) * 5) / 9
        returned = conversion.fahrenheit_to_celsius(397)
        self.assertEqual(returned, expected)

    def test_celsius_to_fahrenheit(self):
        """Tests the Celsius to Fahrenheit Conversion"""

        expected = ((decimal.Decimal(0) * 1.8) + 32)
        returned = conversion.celsius_to_fahrenheit(0)
        self.assertEqual(returned, expected)

    def test_celsius_to_kelvin(self):
        """Tests the Celsius to Kelvin Conversion"""

        expected = decimal.Decimal(971) + decimal.Decimal('273.15')
        returned = conversion.celsius_to_kelvin(971)
        self.assertEqual(returned, expected)

    def test_kelvin_to_celsius(self):
        """Tests the Kelvin to Celsius Conversion"""

        expected = decimal.Decimal(971) - decimal.Decimal('273.15')
        returned = conversion.celsius_to_kelvin(971)
        self.assertEqual(returned, expected)

    def test_fahrenheit_to_kelvin(self):
        """Tests the Fahrenheit to Kelvin Conversion"""
        expected = ((decimal.Decimal(228) - 32) * 5) / 9
        expected += decimal.Decimal('273.15')
        returned = conversion.fahrenheit_to_kelvin(228)
        self.assertEqual(returned, expected)

    def test_kelvin_to_fahrenheit(self):
        """Tests the Kelvin to Fahrenheit Conversion"""
        expected = decimal.Decimal(228) - decimal.Decimal('273.15')
        expected = ((decimal.Decimal(expected) * 1.8) + 32)
        returned = conversion.fahrenheit_to_kelvin(228)
        self.assertEqual(returned, expected)
