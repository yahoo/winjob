#!/usr/bin/env python
# Copyright (c) 2015, Yahoo Inc.
# Copyrights licensed under the BSD
# See the accompanying LICENSE.txt file for terms.
"""
test_winjob
----------------------------------

Tests for `winjob` module.
"""
import unittest


# Any methods of the class below that begin with "test" will be executed
# when the the class is run (by calling unittest.main()
class TestWinjob(unittest.TestCase):

    def test_winjob_import(self):
        import winjob

if __name__ == '__main__':
    unittest.main()
