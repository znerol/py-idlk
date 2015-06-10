from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

BASE41 = "0123456789abcdefghijklmnopqrstuvwxyz-_()$"

def encode(x):
    res = BASE41[x % 41]
    x //= 41
    res = BASE41[x % 41] + res
    x //= 41
    res = BASE41[x % 41] + res
    x //= 41
    res = BASE41[x % 41] + res
    x //= 41
    res = BASE41[x % 41] + res
    x //= 41
    res = BASE41[x] + res
    x //= 41
    assert(x == 0)

    return res

def decode(s):
    b1, b2, b3, b4, b5, b6 = s
    p1 = BASE41.find(b1) * 41 * 41 * 41 * 41 * 41
    assert(p1 >= 0)
    p2 = BASE41.find(b2) * 41 * 41 * 41 * 41
    assert(p2 >= 0)
    p3 = BASE41.find(b3) * 41 * 41 * 41
    assert(p3 >= 0)
    p4 = BASE41.find(b4) * 41 * 41
    assert(p4 >= 0)
    p5 = BASE41.find(b5) * 41
    assert(p5 >= 0)
    p6 = BASE41.find(b6)
    assert(p6 >= 0)

    return p1 + p2 + p3 + p4 + p5 + p6

