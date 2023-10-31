from src.ejercicio1 import *
import pytest

def test_invertirCadena():
    assert invertirCadena("Hola Mundo") == ['o', 'd', 'n', 'u', 'M', ' ', 'a', 'l', 'o', 'H']