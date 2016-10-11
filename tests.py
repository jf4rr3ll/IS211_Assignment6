#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test functions"""

import conversion
import conversionrefactored
import unittest


class TestCases(unittest.TestCase):
    def test_fahrenheit_to_celsius(self):
        """Tests the Fahrenheit to celsius Conversion"""

        expected = 500
        returned = conversion.fahrenheit_to_celsius(932)
        self.assertEqual(returned, expected)
        expected = 490
        returned = conversion.fahrenheit_to_celsius(914)
        self.assertEqual(returned, expected)
        expected = 480
        returned = conversion.fahrenheit_to_celsius(896)
        self.assertEqual(returned, expected)
        expected = 470
        returned = conversion.fahrenheit_to_celsius(878)
        self.assertEqual(returned, expected)
        expected = 460
        returned = conversion.fahrenheit_to_celsius(860)
        self.assertEqual(returned, expected)

    def test_celsius_to_fahrenheit(self):
        """Tests the Celsius to Fahrenheit Conversion"""

        expected = 914
        returned = conversion.celsius_to_fahrenheit(490)
        self.assertEqual(returned, expected)
        expected = 896
        returned = conversion.celsius_to_fahrenheit(480)
        self.assertEqual(returned, expected)
        expected = 878
        returned = conversion.celsius_to_fahrenheit(470)
        self.assertEqual(returned, expected)
        expected = 860
        returned = conversion.celsius_to_fahrenheit(460)
        self.assertEqual(returned, expected)
        expected = 842
        returned = conversion.celsius_to_fahrenheit(450)
        self.assertEqual(returned, expected)

    def test_celsius_to_kelvin(self):
        """Tests the Celsius to Kelvin Conversion"""

        expected = 663.15
        returned = conversion.celsius_to_kelvin(390)
        self.assertEqual(returned, expected)
        expected = 653.15
        returned = conversion.celsius_to_kelvin(380)
        self.assertEqual(returned, expected)
        expected = 643.15
        returned = conversion.celsius_to_kelvin(370)
        self.assertEqual(returned, expected)
        expected = 633.15
        returned = conversion.celsius_to_kelvin(360)
        self.assertEqual(returned, expected)
        expected = 623.15
        returned = conversion.celsius_to_kelvin(350)
        self.assertEqual(returned, expected)

    def test_kelvin_to_celsius(self):
        """Tests the Kelvin to Celsius Conversion"""

        expected = 440
        returned = conversion.kelvin_to_celsius(713.15)
        self.assertEqual(returned, expected)
        expected = 430
        returned = conversion.kelvin_to_celsius(703.15)
        self.assertEqual(returned, expected)
        expected = 420
        returned = conversion.kelvin_to_celsius(693.15)
        self.assertEqual(returned, expected)
        expected = 410
        returned = conversion.kelvin_to_celsius(683.15)
        self.assertEqual(returned, expected)
        expected = 400
        returned = conversion.kelvin_to_celsius(673.15)
        self.assertEqual(returned, expected)

    def test_fahrenheit_to_kelvin(self):
        """Tests the Fahrenheit to Kelvin Conversion"""
        expected = 723.15
        returned = conversion.fahrenheit_to_kelvin(842)
        self.assertEqual(returned, expected)
        expected = 713.15
        returned = conversion.fahrenheit_to_kelvin(824)
        self.assertEqual(returned, expected)
        expected = 703.15
        returned = conversion.fahrenheit_to_kelvin(806)
        self.assertEqual(returned, expected)
        expected = 693.15
        returned = conversion.fahrenheit_to_kelvin(788)
        self.assertEqual(returned, expected)
        expected = 683.15
        returned = conversion.fahrenheit_to_kelvin(770)
        self.assertEqual(returned, expected)

    def test_kelvin_to_fahrenheit(self):
        """Tests the Kelvin to Fahrenheit Conversion"""
        expected = 806
        returned = conversion.kelvin_to_fahrenheit(703.15)
        self.assertEqual(returned, expected)
        expected = 788
        returned = conversion.kelvin_to_fahrenheit(693.15)
        self.assertEqual(returned, expected)
        expected = 770
        returned = conversion.kelvin_to_fahrenheit(683.15)
        self.assertEqual(returned, expected)
        expected = 752
        returned = conversion.kelvin_to_fahrenheit(673.15)
        self.assertEqual(returned, expected)
        expected = 734
        returned = conversion.kelvin_to_fahrenheit(663.15)
        self.assertEqual(returned, expected)

    def tests_convert(self):
        """Tests the conversion function"""
        expected = 623.15
        returned = conversionrefactored.convert('celsius', 'kelvin', 350)
        self.assertEqual(returned, expected)
        expected = 662
        returned = conversionrefactored.convert('celsius', 'fahrenheit', 350)
        self.assertEqual(returned, expected)
        expected = 160
        returned = conversionrefactored.convert('fahrenheit', 'celsius', 320)
        self.assertEqual(returned, expected)
        expected = 433.15
        returned = conversionrefactored.convert('fahrenheit', 'kelvin', 320)
        self.assertEqual(returned, expected)
        expected = 330
        returned = conversionrefactored.convert('kelvin', 'celsius', 603.15)
        self.assertEqual(returned, expected)
        expected = 626
        returned = conversionrefactored.convert('kelvin', 'fahrenheit', 603.15)
        self.assertEqual(returned, expected)
        expected = None
        returned = conversionrefactored.convert('kelvin', 'miles', 100)
        self.assertEqual(returned, expected)
        expected = "Please enter valid conversion units."
        returned = conversionrefactored.convert('meters', 'fahrenheit', 100)
        self.assertEqual(returned, expected)
        expected = None
        returned = conversionrefactored.convert('celsius', 'yards', 100)
        self.assertEqual(returned, expected)

if __name__ == '__main__':
    unittest.main()