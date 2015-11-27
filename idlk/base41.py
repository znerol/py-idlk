"""
Custom Base41 implementation as used for generating idlk file names.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

BASE41 = "0123456789abcdefghijklmnopqrstuvwxyz-_()$"
BASE41_DEC = [
    {char: idx * 41 * 41 * 41 * 41 * 41 for idx, char in enumerate(BASE41)},
    {char: idx * 41 * 41 * 41 * 41 for idx, char in enumerate(BASE41)},
    {char: idx * 41 * 41 * 41 for idx, char in enumerate(BASE41)},
    {char: idx * 41 * 41 for idx, char in enumerate(BASE41)},
    {char: idx * 41 for idx, char in enumerate(BASE41)},
    {char: idx for idx, char in enumerate(BASE41)}
]

class EncodeError(ValueError):
    """
    Raised whenever encoding fails.
    """
    pass

class DecodeError(ValueError):
    """
    Raised whenever decoding fails.
    """
    pass

def encode(value):
    """
    Encodes an integer value and returns a six-character string.
    """
    if value < 0 or value > 41**6-1:
        raise EncodeError('Value out of range')

    result = BASE41[value % 41]
    value //= 41
    result = BASE41[value % 41] + result
    value //= 41
    result = BASE41[value % 41] + result
    value //= 41
    result = BASE41[value % 41] + result
    value //= 41
    result = BASE41[value % 41] + result
    value //= 41
    result = BASE41[value] + result

    return result

def decode(data):
    """
    Decodes a six-character encoded value into an integer.
    """
    if len(data) != 6:
        raise DecodeError('Parameter must be a six-character string')
    try:
        return sum((BASE41_DEC[row][char] for row, char in enumerate(data, 0)))
    except (KeyError, IndexError):
        raise DecodeError('Data out of range')
