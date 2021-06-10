import re
import pytest
import unittest
import wordcount

class TestWordCount:
    def test_enter(self):
        assert 2 == wordcount.findWordCount('hi\nthere')

    def test_tab(self):
        assert 2 == wordcount.findWordCount('hi\tthere')

    def test_astrix(self):
        assert 2 == wordcount.findWordCount('hi\*there')

    def test_comma(self):
        assert 2 == wordcount.findWordCount('hi,there')

    def test_semi(self):
        assert 2 == wordcount.findWordCount('hi;there')

    def test_period(self):
        assert 2 == wordcount.findWordCount('hi.there')
class TestWordCountUnit:
    def test_enter(self):
        self.assertEqual(2, wordcount.findWordCount('hi\nthere'))
        
    def test_tab(self):
        self.assertEqual(2, wordcount.findWordCount('hi\tthere'))

    def test_astrix(self):
        self.assertEqual(2, wordcount.findWordCount('hi\*there'))
                         
    def test_comma(self):
        self.assertEqual(2, wordcount.findWordCount('hi,there'))

    def test_semi(self):
        self.assertEqual(2, wordcount.findWordCount('hi;there'))

    def test_period(self):
        self.assertEqual(2, wordcount.findWordCount('hi.there'))
