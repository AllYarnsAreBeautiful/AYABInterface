"""Conversion of colors to needle positions."""
from collections import namedtuple

NeedlePositions = namedtuple("NeedlePositions", [])


def color_to_needle_positions(rows):
    """Convert rows to needle positions.
    
    :return: 
    :rtype: list
    """
    needles = []
    for row in rows
