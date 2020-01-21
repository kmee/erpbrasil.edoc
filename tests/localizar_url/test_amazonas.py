import unittest

from erpbrasil.edoc.nfe import localizar_url


class TesteHomologacaoAmazonas(unittest.TestCase):
    url_base = 'https://homnfe.sefaz.am.gov.br/'

    def test_inutilizacao(self):
        url_inutilizacao = self.url_base + 'services2/services/' \
                                           'NfeInutilizacao4?wsdl'
        url = localizar_url('NfeInutilizacao', '13')
        self.assertEqual(url, url_inutilizacao)

    def test_consulta_protocolo(self):
        url_consulta_protocolo = self.url_base + 'services2/services/' \
                                                 'NfeConsulta4?wsdl'
        url = localizar_url('NfeConsultaProtocolo', '13')
        self.assertEqual(url, url_consulta_protocolo)

    def test_status_servico(self):
        url_status_servico = self.url_base + 'services2/services/' \
                                             'NfeStatusServico4?wsdl'
        url = localizar_url('NfeStatusServico', '13')
        self.assertEqual(url, url_status_servico)

    def test_recepcao_evento(self):
        url_recepcao_evento = self.url_base + 'services2/services/' \
                                              'RecepcaoEvento4?wsdl'
        url = localizar_url('RecepcaoEvento', '13')
        self.assertEqual(url, url_recepcao_evento)

    def test_autorizacao(self):
        url_autorizacao = self.url_base + 'services2/services/' \
                                          'NfeAutorizacao4?wsdl'
        url = localizar_url('NfeAutorizacao', '13')
        self.assertEqual(url, url_autorizacao)

    def test_consulta_cadastro(self):
        # TODO
        pass

    def test_ret_autorizacao(self):
        url_ret_autorizcao = self.url_base + 'services2/services/' \
                                             'NfeRetAutorizacao4?wsdl'
        url = localizar_url('NfeRetAutorizacao', '13')
        self.assertEqual(url, url_ret_autorizcao)


class TesteProducaoAmazonas(unittest.TestCase):
    url_base = 'https://nfe.sefaz.am.gov.br/'

    def test_inutilizacao(self):
        url_inutilizacao = self.url_base + 'services2/services/' \
                                           'NfeInutilizacao4?wsdl'
        url = localizar_url('NfeInutilizacao', '13', ambiente=1)
        self.assertEqual(url, url_inutilizacao)

    def test_consulta_protocolo(self):
        url_consulta_protocolo = self.url_base + 'services2/services/' \
                                                 'NfeConsulta4?wsdl'
        url = localizar_url('NfeConsultaProtocolo', '13', ambiente=1)
        self.assertEqual(url, url_consulta_protocolo)

    def test_status_servico(self):
        url_status_servico = self.url_base + 'services2/services/' \
                                             'NfeStatusServico4?wsdl'
        url = localizar_url('NfeStatusServico', '13', ambiente=1)
        self.assertEqual(url, url_status_servico)

    def test_recepcao_evento(self):
        url_recepcao_evento = self.url_base + 'services2/services/' \
                                              'RecepcaoEvento4?wsdl'
        url = localizar_url('RecepcaoEvento', '13', ambiente=1)
        self.assertEqual(url, url_recepcao_evento)

    def test_autorizacao(self):
        url_autorizacao = self.url_base + 'services2/services/' \
                                          'NfeAutorizacao4?wsdl'
        url = localizar_url('NfeAutorizacao', '13', ambiente=1)
        self.assertEqual(url, url_autorizacao)

    def test_consulta_cadastro(self):
        # TODO
        pass

    def test_ret_autorizacao(self):
        url_ret_autorizcao = self.url_base + 'services2/services/' \
                                             'NfeRetAutorizacao4?wsdl'
        url = localizar_url('NfeRetAutorizacao', '13', ambiente=1)
        self.assertEqual(url, url_ret_autorizcao)


if __name__ == '__main__':
    unittest.main()
