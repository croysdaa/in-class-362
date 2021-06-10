import re
import pytest
import unittest
import wordcount

def test_enter():
    assert findWordCount('hi\nthere') == 2
    
def test_tab():
    assert findWordCount('hi\tthere') == 2
    
def test_astrix():
    assert findWordCount('hi\*there') == 2
    
def test_comma():
    assert findWordCount('hi,there') == 2
    
def test_semi():
    assert findWordCount('hi;there') == 2
    
def test_period():
    assert findWordCount('hi.there') == 2
