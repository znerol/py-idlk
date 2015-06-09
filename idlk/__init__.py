import os.path
import idlk.base41

def hash_macroman(data):
    h = 0
    for c in data:
        h = ((h << 8) + h) + ord(c)

    return h % 0xFFFEECED

def idlk(filename):
    # Convert to lowercase first.
    filename = filename.lower()

    # The original algorithm seems to prefer Mac Roman encoding as long as
    # there are no non-mappable characters in the file name.
    try:
        macroman_name = filename.encode('macroman')
    except UnicodeEncodeError:
        pass
    finally:
        hashed = base41.encode(hash_macroman(macroman_name))
        base, ext = os.path.splitext(macroman_name)
        return u"~{:s}~{:s}.idlk".format(base[0:18].decode('macroman'), hashed)

    # Regrettably the encoding / hashing algorithm for unicode filenames is
    # not currently known. Please file a feature request/patch if you
    # discover a working implementation.
    return False
