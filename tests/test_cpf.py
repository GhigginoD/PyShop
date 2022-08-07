import pytest
from source.cpf import Cpf

def test_deve_verificar_se_e_um_cpf_valido_com_pontuacao():
    with pytest.raises(Exception) as exception:   
        Cpf('379.757.400-22')
        assert "cpf invalid" in str(exception.value)
        assert exception.type == ValueError

def test_deve_verificar_se_e_um_cpf_valido_sem_pontuacao():

    with pytest.raises(Exception) as exception:   
        Cpf('04296765061')
        assert "cpf invalid" in str(exception.value)
        assert exception.type == ValueError
    
def test_deve_verificar_se_e_um_valor_em_branco(): 
    with pytest.raises(Exception) as exception:   
        Cpf('')
        assert "cpf empty" in str(exception.value)
        assert exception.type == ValueError

def test_deve_verificar_quantidade_de_caracteres():
    with pytest.raises(Exception) as exception:   
        Cpf('123.456.789-10')
        assert "wrong cpf size" in str(exception.value)
        assert exception.type == ValueError

def test_deve_validar_um_cpf_correto():
    assert Cpf('175.862.060-90')


