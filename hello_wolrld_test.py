"""Tests de hello world"""

import hello_world

def test_saludo():
    """Pruebas de saludo"""
    assert hello_world.saluda("Yama") == "¡Hola Yama!"
    assert hello_world.saluda("Luis") == "¡Hola Luis!"
    