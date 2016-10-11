#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides various temperature conversions"""


ABSOLUTE_DIFFERENCE = 273.15


def fahrenheit_to_celsius(degrees):
    """Defines a function that converts Fahrenheit to Celsius.
    Args:
        degrees (float): Degrees in Fahrenheit.
    Returns:
        decimal: Degrees converted to Celsius.
    Examples:
        >>> fahrenheit_to_celsius(212)
        Decimal('100')
        >>> fahrenheit_to_celsius(32)
        Decimal('0')
    """

    return (degrees - 32) * 5 / 9

def celsius_to_fahrenheit(degrees):
    """Defines a function that converts Fahrenheit to Celsius.
    Args:
        degrees (float): Degrees in Fahrenheit.
    Returns:
        decimal: Degrees converted to Celsius.
    Examples:
        >>> celsius_to_fahrenheit(100)
        Decimal('212')
        >>> celsius_to_fahrenheit(0)
        Decimal('32')
    """
    return (degrees * 1.8) + 32

def celsius_to_kelvin(degrees):
    """Defines a function that converts Celsius to Kelvin
    Args:
        degrees (float): Degrees in Celsius.
    Returns:
        decimal: Degrees converted to Kelvin.
    Examples:
        >>> celsius_to_kelvin(100)
        Decimal('373.15')
        >>> celsius_to_kelvin(0)
        Decimal('273.15')
    """

    return degrees + ABSOLUTE_DIFFERENCE

def kelvin_to_celsius(degrees):
    """Defines a function that converts Celsius to Kelvin
    Args:
        degrees (float): Degrees in Celsius.
    Returns:
        decimal: Degrees converted to Kelvin.
    Examples:
        >>> kelvin_to_celsius(0)
        Decimal('-273.15')
        >>> kelvin_to_celsius(150)
        Decimal('123.15')
    """

    return degrees - ABSOLUTE_DIFFERENCE


def fahrenheit_to_kelvin(degrees):
    """Defines a function that converts Fahrenheit to Kelvin
    Args:
        degrees (float): Degrees in Fahrenheit
    Returns:
        decimal: Degrees convertet to Kelvin
    Examples:
        >>> fahrenheit_to_kelvin(212)
        Decimal('373.15')
        >>>fahrenheit_to_kelvin(32)
        Decimal('273.16')
    """

    return celsius_to_kelvin(fahrenheit_to_celsius(degrees))


def kelvin_to_fahrenheit(degrees):
    """Defines a function that converts Fahrenheit to Kelvin
    Args:
        degrees (float): Degrees in Fahrenheit
    Returns:
        decimal: Degrees convertet to Kelvin
    Examples:
        >>> fahrenheit_to_kelvin(212)
        Decimal('373.15')
        >>>fahrenheit_to_kelvin(32)
        Decimal('273.16')
    """

    return celsius_to_fahrenheit(kelvin_to_celsius(degrees))

def meters_to_yards(dist):
    return dist * 1.09361

def yards_to_meters(dist):
    return dist * 0.9144

def meters_to_miles(dist):
    return dist * 0.000621371

def miles_to_meters(dist):
    return dist * 1609.34

def yards_to_miles(dist):
    return dist * 0.000568182

def miles_to_yards(dist):
    return dist * 1760