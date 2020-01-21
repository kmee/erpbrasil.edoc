import unittest

from erpbrasil.edoc.nfe import localizar_url


class TesteHomologacaoAmbienteNacional(unittest.TestCase):

    def test_distribuicao(self):
        url_distribuicao = 'https://hom.nfe.fazenda.gov.br/' \
                           'NFeDistribuicaoDFe/NFeDistribuicaoDFe.asmx?wsdl'
        url = localizar_url('NFeDistribuicaoDFe', '91')
        self.assertEqual(url, url_distribuicao)

    def test_recepcao_evento(self):
        url_recepcao = 'https://hom.nfe.fazenda.gov.br/' \
            'NFeRecepcaoEvento4/NFeRecepcaoEvento4.asmx?wsdl'
        url = localizar_url('RecepcaoEvento', '91')
        self.assertEqual(url, url_recepcao)


class TesteProducaoAmbienteNacional(unittest.TestCase):

    def test_distribuicao(self):
        url_distribuicao = 'https://nfe.fazenda.gov.br/' \
                           'NFeDistribuicaoDFe/NFeDistribuicaoDFe.asmx?wsdl'
        url = localizar_url('NFeDistribuicaoDFe', '91', ambiente=1)
        self.assertEqual(url, url_distribuicao)
