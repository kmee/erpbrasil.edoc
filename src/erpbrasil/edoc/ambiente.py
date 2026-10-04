# License MIT
"""Normalização do ambiente (produção x homologação) em toda a biblioteca.

O valor canônico é o texto do ``tpAmb`` do leiaute: ``"1"`` (produção) ou
``"2"`` (homologação). Quem chama pode passar inteiro ou texto.
"""

AMBIENTE_PRODUCAO = "1"
AMBIENTE_HOMOLOGACAO = "2"

_VALIDOS = {
    1: AMBIENTE_PRODUCAO,
    2: AMBIENTE_HOMOLOGACAO,
    "1": AMBIENTE_PRODUCAO,
    "2": AMBIENTE_HOMOLOGACAO,
}


def normalizar_ambiente(ambiente):
    """Devolve ``"1"`` ou ``"2"`` para 1, 2, "1" ou "2"; ValueError nos demais."""
    # só int e str: bool, float e afins (True == 1, 1.0 == 1) não são ambiente
    if type(ambiente) in (int, str) and ambiente in _VALIDOS:
        return _VALIDOS[ambiente]
    raise ValueError(
        f"Ambiente inválido: {ambiente!r}. Use 1 (produção) ou 2 (homologação), "
        'como inteiro ou texto ("1" ou "2").'
    )


def em_producao(ambiente):
    """True se o ambiente é produção; valida o valor recebido."""
    return normalizar_ambiente(ambiente) == AMBIENTE_PRODUCAO
