import pytest
from escola import v_media

def test_aprovado():
    assert v_media(8) == "aprovado"