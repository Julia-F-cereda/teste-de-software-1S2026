import pytest
from escola import v_media

def test_string():
    with pytest.raises(TypeError, match="Tipo inválido, a entrada deve ser numerica"):
        v_media("oito")

def test_value_menor():
    with pytest.raises(ValueError, match="Valor invalido, entrada tem que ser maior que 0"):
        v_media(-5)

def test_value_maior():
    with pytest.raises(ValueError, match="Valor invalido, entrada tem que ser menor que 10"):
        v_media(2000)

