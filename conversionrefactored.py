#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test functions"""

import conversion


def convert(fromUnit, toUnit, value):
    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()
    temp = ['celsius', 'fahrenheit', 'kelvin']
    dist = ['meters', 'miles', 'yards']
    tempfuncs = [conversion.celsius_to_fahrenheit(value), conversion.celsius_to_kelvin(value),
                 conversion.fahrenheit_to_celsius(value), conversion.fahrenheit_to_kelvin(value),
                 conversion.kelvin_to_celsius(value), conversion.kelvin_to_fahrenheit(value)]
    distfuncs = [conversion.meters_to_miles(value), conversion.meters_to_yards(value),
                 conversion.miles_to_meters(value), conversion.miles_to_yards(value),
                 conversion.yards_to_meters(value), conversion.yards_to_miles(value)]

    if fromUnit == toUnit:
        return value

    if fromUnit and toUnit in temp:
        if fromUnit == temp[0]:
            if toUnit == temp[1]:
                return tempfuncs[0]
            if toUnit == temp[2]:
                return tempfuncs[1]
        if fromUnit == temp[1]:
            if toUnit == temp[0]:
                return tempfuncs[2]
            if toUnit == temp[2]:
                return tempfuncs[3]
        if fromUnit == temp[2]:
            if toUnit == temp[0]:
                return tempfuncs[4]
            if toUnit == temp[1]:
                return tempfuncs[5]

    if fromUnit and toUnit in dist:
        if fromUnit == dist[0]:
            if toUnit == dist[1]:
                return distfuncs[0]
            if toUnit == dist[2]:
                return distfuncs[1]
        if fromUnit == dist[1]:
            if toUnit == dist[0]:
                return distfuncs[2]
            if toUnit == dist[2]:
                return distfuncs[3]
        if fromUnit == dist[2]:
            if toUnit == dist[0]:
                return distfuncs[4]
            if toUnit == dist[1]:
                return distfuncs[5]

    else:
        return "Please enter valid conversion units."