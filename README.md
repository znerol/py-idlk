# Python idlk

[![Build Status](https://travis-ci.org/znerol/py-idlk.svg?branch=master)](https://travis-ci.org/znerol/py-idlk)
[![Coverage Status](https://coveralls.io/repos/github/znerol/py-idlk/badge.svg?branch=master)](https://coveralls.io/github/znerol/py-idlk?branch=master)

This is a proof-of-concept implementation of a lock filename generator for idlk
files used by a well known desktop publishing suite.


## Usage

```
    from idlk import idlk

    lockname = idlk(u'My Layout File.INDD')
    # lockname == u'~my layout file~q7e)nv.idlk'

    lockname = idlk(u'My Text.icml')
    # lockname == u'~my text~7h5m7u.idlk'
```


## Technical details

The names of the lockfiles are derived from a given file name with the
following steps:

1. Apply NFC unicode normalization.
2. Convert the complete filename to lower case.
3. Switch to Mac Roman encoding.
4. Generate a 32bit hash value over the whole file name and encode it using a
   custom base41 encoding scheme.
5. Remove extension from the prepared file name, shorten it further to 18
   characters if necessary.
6. Generate the idlk file name using the following pattern:
   ~shortened-lowercase-basename[1..18]~hash[6].idlk

Note: Even though the hash-function is rather primitive, there is no way of
directly deriving the original document name for a given idlk name.


### Hash function

The hash function is a very simple shift-add function. The only tricky/weird
thing is a final modulo with the magic number `0xFFFEECED`.


### Base41 encoding

Base41 produces a case insensitive string containing digits `0-9`, characters
`a-z` and the 5 additional characters `-`, `_`, `(`, `)` and `$`.


## Caveats

The algorithm has been deduced after observing the behavior of the original
software. It currently only works with file names which are completely mappable
to the Mac Roman encoding.


## License

All code and documentation is released under the MIT license.
