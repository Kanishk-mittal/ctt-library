#!/usr/bin/env python

"""Tests for `cyphertext` package."""


import unittest

from cyphertext.encoder import *


class TestCyphertext(unittest.TestCase):
    """Tests for `cyphertext` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""
    def test_ceaser_001(self):
        self.assertEqual(ceaser('Hello, World!', 3), 'KHOOR, ZRUOG!')
    def test_ceaser_002(self):
        self.assertEqual(ceaser('Hello, World!', 0), 'HELLO, WORLD!')
    def test_ceaser_003(self):
        self.assertEqual(ceaser('Hello, World!', 26), 'HELLO, WORLD!')
    def test_ceaser_004(self):
        self.assertEqual(ceaser('Hello, World!', 27), 'IFMMP, XPSME!')
    def test_ceaser_005(self):
        self.assertEqual(ceaser('Hello, World!', 128), 'FCJJM, UMPJB!')
    def test_ceaser_006(self):
        self.assertEqual(ceaser('Hello, World!', -3), 'EBIIL, TLOIA!')
