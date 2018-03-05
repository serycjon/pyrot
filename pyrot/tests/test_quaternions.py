from unittest import TestCase

import pyrot

class TestJoke(TestCase):
    def test_is_string(self):
        s = pyrot.joke()
        self.assertTrue(isinstance(s, basestring))
