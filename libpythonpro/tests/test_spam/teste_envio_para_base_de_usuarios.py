from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.teste_enviador_de_email import Enviador


def test_envio_de_spam(sessao=None):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'gedsao77@hotmail.com',
        'rodrigobuenoguedes@gmail.com',
        'Confira comigo'
    )