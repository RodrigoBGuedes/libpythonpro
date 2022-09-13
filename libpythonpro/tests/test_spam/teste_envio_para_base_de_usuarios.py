from unittest.mock import Mock

import pytest
from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Rodrigo', email='foo@bar.com.br'),
            Usuario(nome='Geraldo', email='gee@bar.com.br')
        ],
        [
            Usuario(nome='Rodrigo', email='foo@bar.com.br')
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'foo@bar.com.br',
        'Curso Python Pro',
        'Confira os Modulos Fantasticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Rodrigo', email='foo@bar.com.br')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'gee@bar.com.br',
        'Curso Python Pro',
        'Confira os Modulos Fantasticos'
    )
    enviador.enviar.assert_called_once_with(
        'gee@bar.com.br',
        'foo@bar.com.br',
        'Curso Python Pro',
        'Confira os Modulos Fantasticos'
    )
