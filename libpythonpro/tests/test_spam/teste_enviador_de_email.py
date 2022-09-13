import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['gedsao77@hotmail.com', 'rodrigo-guedes@hotmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'rodrigobuenoguedes@gmail.com',
        'Cursos Python Pro',
        'Teste Doidera é isso'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'geraldo']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'rodrigobuenoguedes@gmail.com',
            'Cursos Python Pro',
            'Teste Doidera é isso'
        )
