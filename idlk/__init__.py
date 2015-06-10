from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import os
import sys
import idlk.base41

if sys.version_info[0] == 3:
    _get_byte = lambda c: c
else:
    _get_byte = ord

def hash_macroman(data):
    h = 0
    for c in data:
        h = ((h << 8) + h) + _get_byte(c)

    return h % 0xFFFEECED

def idlk(filename):
    # Convert to lowercase first.
    filename = filename.lower()

    # The original algorithm seems to prefer Mac Roman encoding as long as
    # there are no non-mappable characters in the file name.
    try:
        macroman_name = filename.encode("macroman")
    except UnicodeEncodeError:
        pass
    finally:
        hashed = base41.encode(hash_macroman(macroman_name))
        base, ext = os.path.splitext(macroman_name)
        return "~{:s}~{:s}.idlk".format(base[0:18].decode("macroman"), hashed)

    # Regrettably the encoding / hashing algorithm for unicode filenames is
    # not currently known. Please file a feature request/patch if you
    # discover a working implementation.
    return False
