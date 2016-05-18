import pytest
import sys
sys.path.append("../src/")
import blockprint as bp


def test_height_of_block():
    string = "1 \n 245\n3"
    assert bp.height_of_block(string) == 3

def test_width_of_block():
    string = "1 \n 245\n3"
    assert bp.width_of_block(string) == 4

def test_shape():
    liste = [["a",], ["a\nb", "aaa"], ["aa\naa", "b"]]
    assert bp.shape(liste) == (3, 2)

def test_maxsizes():
    liste = [["a",], ["a\nb", "aaa"], ["aa\naa", "b"]]
    assert bp.maxsizes(liste) == ([1, 2, 2], [2, 3])

def test_block():
    liste = [["a",], ["a\nb", "aaa"], ["aa\naa", "b"]]
    assert bp.block(liste) == " a\n aaaa\n b\naa  b\naa\n"

