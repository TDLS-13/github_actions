import pytest


def test_calc_addition():
    # fonction test 2+4
    output = 2+4
    assert output == 6


def test_calc_substraction():
    # fonction test du resultat 2-4
    output = 2-4
    assert output == -2


def test_calc_multiply():
    # resultat de 2*4
    output = 2*4
    assert output == 8


def test_coucou():
    # return hello
    output = 'hello'
    assert output == 'hello'
