from third_project.math_relatif import plus, moins
import pytest


def test_plus():
    assert plus(2, 2) == 4

def test_moins():
    assert moins(5, 1) == 4
