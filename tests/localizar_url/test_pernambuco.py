import unittest

from erpbrasil.edoc.nfe import localizar_url


class TesteHomologacaoPernambuco(unittest.TestCase):
    url_base = 'https://nfehomolog.sefaz.pe.gov.br/'

    def test_inutilizacao(self):
        url_inutilizacao = self.url_base + 'nfe-service/services/NFeInutilizacao4?wsdl'
        url = localizar_url('NfeInutilizacao', '26')
        self.assertEqual(url, url_inutilizacao)

    def test_consulta_protocolo(self):
        url_consulta_protocolo = self.url_base + 'nfe-service/services/' \
                                                 'NFeConsultaProtocolo4?wsdl'
        url = localizar_url('NfeConsultaProtocolo', '26')
        self.assertEqual(url, url_consulta_protocolo)

    def test_status_servico(self):
        url_status_servico = self.url_base + 'nfe-service/services/' \
                                             'NFeStatusServico4?wsdl'
        url = localizar_url('NfeStatusServico', '26')
        self.assertEqual(url, url_status_servico)

    def test_recepcao_evento(self):
        url_recepcao_evento = self.url_base + 'nfe-service/services/' \
                                              'NFeRecepcaoEvento4?wsdl'
        url = localizar_url('RecepcaoEvento', '26')
        self.assertEqual(url, url_recepcao_evento)

    def test_autorizacao(self):
        url_autorizacao = self.url_base + 'nfe-service/services/NFeAutorizacao4?wsdl'
        url = localizar_url('NfeAutorizacao', '26')
        self.assertEqual(url, url_autorizacao)

    def test_consulta_cadastro(self):
        url_consulta_cadastro = self.url_base + 'nfe-service/services/' \
                                                'CadConsultaCadastro4?wsdl'
        url = localizar_url('NfeConsultaCadastro', '26')
        self.assertEqual(url, url_consulta_cadastro)

    def test_ret_autorizacao(self):
        url_ret_autorizcao = self.url_base + 'nfe-service/services/' \
                                             'NFeRetAutorizacao4?wsdl'
        url = localizar_url('NfeRetAutorizacao', '26')
        self.assertEqual(url, url_ret_autorizcao)


class TesteProducaoPernambuco(unittest.TestCase):
    url_base = 'https://nfe.sefaz.pe.gov.br/'

    def test_inutilizacao(self):
        url_inutilizacao = self.url_base + 'nfe-service/services/' \
                                           'NFeInutilizacao4?wsdl'
        url = localizar_url('NfeInutilizacao', '26', ambiente=1)
        self.assertEqual(url, url_inutilizacao)

    def test_consulta_protocolo(self):
        url_consulta_protocolo = self.url_base + 'nfe-service/services/' \
                                                 'NFeConsultaProtocolo4?wsdl'
        url = localizar_url('NfeConsultaProtocolo', '26', ambiente=1)
        self.assertEqual(url, url_consulta_protocolo)

    def test_status_servico(self):
        url_status_servico = self.url_base + 'nfe-service/services/' \
                                             'NFeStatusServico4?wsdl'
        url = localizar_url('NfeStatusServico', '26', ambiente=1)
        self.assertEqual(url, url_status_servico)

    def test_recepcao_evento(self):
        url_recepcao_evento = self.url_base + 'nfe-service/services/' \
                                              'NFeRecepcaoEvento4?wsdl'
        url = localizar_url('RecepcaoEvento', '26', ambiente=1)
        self.assertEqual(url, url_recepcao_evento)

    def test_autorizacao(self):
        url_autorizacao = self.url_base + 'nfe-service/services/NFeAutorizacao4?wsdl'
        url = localizar_url('NfeAutorizacao', '26', ambiente=1)
        self.assertEqual(url, url_autorizacao)

    def test_consulta_cadastro(self):
        url_consulta_cadastro = self.url_base + 'nfe-service/services/' \
                                                'CadConsultaCadastro4?wsdl'
        url = localizar_url('NfeConsultaCadastro', '26', ambiente=1)
        self.assertEqual(url, url_consulta_cadastro)

    def test_ret_autorizacao(self):
        url_ret_autorizcao = self.url_base + 'nfe-service/services/' \
                                             'NFeRetAutorizacao4?wsdl'
        url = localizar_url('NfeRetAutorizacao', '26', ambiente=1)
        self.assertEqual(url, url_ret_autorizcao)


if __name__ == '__main__':
    unittest.main()
