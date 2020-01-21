import unittest

from erpbrasil.edoc.nfe import localizar_url


class TesteHomologacaoPara(unittest.TestCase):
    url_base = 'https://hom.sefazvirtual.fazenda.gov.br/'

    def test_inutilizacao(self):
        url_inutilizacao = self.url_base + 'NFeInutilizacao4/' \
            'NFeInutilizacao4.asmx?wsdl'
        url = localizar_url('NfeInutilizacao', '15')
        self.assertEqual(url, url_inutilizacao)

    def test_consulta_protocolo(self):
        url_consulta_protocolo = self.url_base + 'NFeConsultaProtocolo4/' \
            'NFeConsultaProtocolo4.asmx?wsdl'
        url = localizar_url('NfeConsultaProtocolo', '15')
        self.assertEqual(url, url_consulta_protocolo)

    def test_status_servico(self):
        url_status_servico = self.url_base + 'NFeStatusServico4/' \
            'NFeStatusServico4.asmx?wsdl'
        url = localizar_url('NfeStatusServico', '15')
        self.assertEqual(url, url_status_servico)

    def test_recepcao_evento(self):
        url_recepcao_evento = self.url_base + 'NFeRecepcaoEvento4/' \
            'NFeRecepcaoEvento4.asmx?wsdl'
        url = localizar_url('RecepcaoEvento', '15')
        self.assertEqual(url, url_recepcao_evento)

    def test_autorizacao(self):
        url_autorizacao = self.url_base + 'NFeAutorizacao4/' \
            'NFeAutorizacao4.asmx?wsdl'
        url = localizar_url('NfeAutorizacao', '15')
        self.assertEqual(url, url_autorizacao)

    def test_ret_autorizacao(self):
        url_ret_autorizcao = self.url_base + 'NFeRetAutorizacao4/' \
                                             'NFeRetAutorizacao4.asmx?wsdl'
        url = localizar_url('NfeRetAutorizacao', '15')
        self.assertEqual(url, url_ret_autorizcao)


class TesteProducaoPara(unittest.TestCase):
    url_base = 'https://www.sefazvirtual.fazenda.gov.br/'

    def test_inutilizacao(self):
        url_inutilizacao = self.url_base + 'NFeInutilizacao4/' \
                                           'NFeInutilizacao4.asmx?wsdl'
        url = localizar_url('NfeInutilizacao', '15', ambiente=1)
        self.assertEqual(url, url_inutilizacao)

    def test_consulta_protocolo(self):
        url_consulta_protocolo = self.url_base + 'NFeConsultaProtocolo4/' \
                                                 'NFeConsultaProtocolo4.asmx?wsdl'
        url = localizar_url('NfeConsultaProtocolo', '15', ambiente=1)
        self.assertEqual(url, url_consulta_protocolo)

    def test_status_servico(self):
        url_status_servico = self.url_base + 'NFeStatusServico4/' \
                                             'NFeStatusServico4.asmx?wsdl'
        url = localizar_url('NfeStatusServico', '15', ambiente=1)
        self.assertEqual(url, url_status_servico)

    def test_recepcao_evento(self):
        url_recepcao_evento = self.url_base + 'NFeRecepcaoEvento4/' \
                                              'NFeRecepcaoEvento4.asmx?wsdl'
        url = localizar_url('RecepcaoEvento', '15', ambiente=1)
        self.assertEqual(url, url_recepcao_evento)

    def test_autorizacao(self):
        url_autorizacao = self.url_base + 'NFeAutorizacao4/' \
                                          'NFeAutorizacao4.asmx?wsdl'
        url = localizar_url('NfeAutorizacao', '15', ambiente=1)
        self.assertEqual(url, url_autorizacao)

    def test_ret_autorizacao(self):
        url_ret_autorizcao = self.url_base + 'NFeRetAutorizacao4/' \
                                             'NFeRetAutorizacao4.asmx?wsdl'
        url = localizar_url('NfeRetAutorizacao', '15', ambiente=1)
        self.assertEqual(url, url_ret_autorizcao)


if __name__ == '__main__':
    unittest.main()
