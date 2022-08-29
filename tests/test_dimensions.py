from source.dimension import Dimension
import pytest

from source.item import Item

def test_deve_gerar_erro_ao_criar_com_peso_negativo():
    with pytest.raises(Exception) as exception:   
        Dimension(-1,1,2,3)
        assert "invalid dimensions" in str(exception.value)

def test_deve_gerar_erro_ao_criar_com_largura_negativa():
    with pytest.raises(Exception) as exception:   
        Dimension(1,-1,2,3)
        assert "invalid dimensions" in str(exception.value)

def test_deve_gerar_erro_ao_criar_com_cumprimento_negativo():
    with pytest.raises(Exception) as exception:   
        Dimension(1,1,-2,3)
        assert "invalid dimensions" in str(exception.value)

def test_deve_gerar_erro_ao_criar_com_altura_negativa():
    with pytest.raises(Exception) as exception:   
        Dimension(1,1,2,-3)
        assert "invalid dimensions" in str(exception.value)