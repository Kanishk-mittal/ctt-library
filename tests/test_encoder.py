#!/usr/bin/env python

"""Tests for `cyphertext` package."""


import unittest

from cyphertext import encoder


class TestEncoder(unittest.TestCase):
    """Tests for `encoder` package."""

    # caesar
    def test_Caesar_001(self):
        self.assertEqual(encoder.caesar('Hello, World!', 3), 'KHOOR, ZRUOG!')
    def test_Caesar_002(self):
        self.assertEqual(encoder.caesar('Hello, World!', 0), 'HELLO, WORLD!')
    def test_Caesar_003(self):
        self.assertEqual(encoder.caesar('Hello, World!', 26), 'HELLO, WORLD!')
    def test_Caesar_004(self):
        self.assertEqual(encoder.caesar('Hello, World!', 27), 'IFMMP, XPSME!')
    def test_Caesar_005(self):
        self.assertEqual(encoder.caesar('Hello, World!', 128), 'FCJJM, UMPJB!')
    def test_Caesar_006(self):
        self.assertEqual(encoder.caesar('Hello, World!', -3), 'EBIIL, TLOIA!')
    
    # Piglatin
    def test_Piglatin_001(self):
        self.assertEqual(encoder.piglatin('Hello, World!'), 'elloHay, orldWay!')
    def test_Piglatin_002(self):
        self.assertEqual(encoder.piglatin('Python is fun'), 'onPythay isyay unfay')
    def test_Piglatin_003(self):
        self.assertEqual(encoder.piglatin('Coding is awesome'), 'odingCay isyay awesomeyay')
    def test_Piglatin_004(self):
        self.assertEqual(encoder.piglatin('GitHub Copilot'), 'itHubGay opilotCay')
    def test_Piglatin_005(self):
        self.assertEqual(encoder.piglatin('Artificial Intelligence'), 'Artificialyay Intelligenceyay')
    # Affine
    def test_Affine_001(self):
        self.assertEqual(encoder.affine('A quick brown fox, suddenly jumped over a lazy dog !', 3, 7), 'H DPFNL KGXVU WXY, JPQQTUOB IPRATQ XSTG H OHEB QXZ !')
    def test_Affine_002(self):
        self.assertEqual(encoder.affine('A quick brown fox, suddenly jumped over a lazy dog !', 1, 0), 'A QUICK BROWN FOX, SUDDENLY JUMPED OVER A LAZY DOG !')
    def test_Affine_003(self):
        self.assertEqual(encoder.affine('A quick brown fox, suddenly jumped over a lazy dog !', 5, 12), 'M OIAWK RTESZ LEX, YIBBGZPC FIUJGB ENGT M PMHC BEQ !')
    def test_Affine_004(self):
        self.assertEqual(encoder.affine('A quick brown fox, suddenly jumped over a lazy dog !', 9, 21), 'V JTPNH ESRLI ORU, BTWWFIQD YTZAFW RCFS V QVMD WRX !')
    def test_Affine_005(self):
        self.assertEqual(encoder.affine('A quick brown fox, suddenly jumped over a lazy dog !', 25, 3), 'D NJVBT CMPHQ YPG, LJAAZQSF UJROZA PIZM D SDEF APX !')