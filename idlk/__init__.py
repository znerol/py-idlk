"""
A lock filename generator for idlk files used by a well known DTP suite.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import os
import sys
import unicodedata
from idlk import base41

if sys.version_info[0] == 3:
    _get_byte = lambda c: c
else:
    _get_byte = ord

class IdlkError(ValueError):
    """
    Raised whenever filename generation fails.
    """
    pass

def hash_macroman(data):
    """
    Compute the hash for the given byte string.
    """
    result = 0
    for char in data:
        result = ((result << 8) + result) + _get_byte(char)

    return result % 0xFFFEECED

def idlk(filename):
    """
    Generate the lock file name for the given file.
    """

    # Normalize to NFC.
    filename = unicodedata.normalize('NFC', filename)

    # Convert to lowercase first.
    filename = filename.lower()

    # The original algorithm seems to prefer Mac Roman encoding as long as
    # there are no non-mappable characters in the file name.
    try:
        macroman_name = filename.encode("macroman")
    except UnicodeEncodeError:
        # Regrettably the encoding / hashing algorithm for unicode filenames is
        # not currently known. Please file a feature request/patch if you
        # discover a working implementation.
        raise IdlkError("File names with characters outside the Mac OS Roman "
                        "encoding are not supported")
    else:
        hashed = base41.encode(hash_macroman(macroman_name))
        base = os.path.splitext(macroman_name)[0]
        return "~{:s}~{:s}.idlk".format(base[0:18].decode("macroman"), hashed)
