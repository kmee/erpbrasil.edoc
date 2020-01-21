import unittest

from erpbrasil.edoc.nfe import localizar_url


class TesteHomologacaoCeara(unittest.TestCase):
    url_base = 'https://nfeh.sefaz.ce.gov.br/'

    def test_inutilizacao(self):
        url_inutilizacao = self.url_base + 'nfe4/services/' \
                                           'NFeInutilizacao4?wsdl'
        url = localizar_url('NfeInutilizacao', '23')
        self.assertEqual(url, url_inutilizacao)

    def test_consulta_protocolo(self):
        url_consulta_protocolo = self.url_base + 'nfe4/services/' \
                                                 'NFeConsultaProtocolo4?wsdl'
        url = localizar_url('NfeConsultaProtocolo', '23')
        self.assertEqual(url, url_consulta_protocolo)

    def test_status_servico(self):
        url_status_servico = self.url_base + 'nfe4/services/' \
                                             'NFeStatusServico4?wsdl'
        url = localizar_url('NfeStatusServico', '23')
        self.assertEqual(url, url_status_servico)

    def test_recepcao_evento(self):
        url_recepcao_evento = self.url_base + 'nfe4/services/' \
                                              'NFeRecepcaoEvento4?wsdl'
        url = localizar_url('RecepcaoEvento', '23')
        self.assertEqual(url, url_recepcao_evento)

    def test_autorizacao(self):
        url_autorizacao = self.url_base + 'nfe4/services/NFeAutorizacao4?wsdl'
        url = localizar_url('NfeAutorizacao', '23')
        self.assertEqual(url, url_autorizacao)

    def test_consulta_cadastro(self):
        url_consulta_cadastro = self.url_base + 'nfe4/services/' \
                                                'CadConsultaCadastro4?wsdl'
        url = localizar_url('NfeConsultaCadastro', '23')
        self.assertEqual(url, url_consulta_cadastro)

    def test_ret_autorizacao(self):
        url_ret_autorizcao = self.url_base + 'nfe4/services/' \
                                             'NFeRetAutorizacao4?wsdl'
        url = localizar_url('NfeRetAutorizacao', '23')
        self.assertEqual(url, url_ret_autorizcao)


class TesteProducaoCeara(unittest.TestCase):
    url_base = 'https://nfe.sefaz.ce.gov.br/'

    def test_inutilizacao(self):
        url_inutilizacao = self.url_base + 'nfe4/services/' \
                                           'NFeInutilizacao4?wsdl'
        url = localizar_url('NfeInutilizacao', '23', ambiente=1)
        self.assertEqual(url, url_inutilizacao)

    def test_consulta_protocolo(self):
        url_consulta_protocolo = self.url_base + 'nfe4/services/' \
                                                 'NFeConsultaProtocolo4?wsdl'
        url = localizar_url('NfeConsultaProtocolo', '23', ambiente=1)
        self.assertEqual(url, url_consulta_protocolo)

    def test_status_servico(self):
        url_status_servico = self.url_base + 'nfe4/services/' \
                                             'NFeStatusServico4?wsdl'
        url = localizar_url('NfeStatusServico', '23', ambiente=1)
        self.assertEqual(url, url_status_servico)

    def test_recepcao_evento(self):
        url_recepcao_evento = self.url_base + 'nfe4/services/' \
                                              'NFeRecepcaoEvento4?wsdl'
        url = localizar_url('RecepcaoEvento', '23', ambiente=1)
        self.assertEqual(url, url_recepcao_evento)

    def test_autorizacao(self):
        url_autorizacao = self.url_base + 'nfe4/services/NFeAutorizacao4?wsdl'
        url = localizar_url('NfeAutorizacao', '23', ambiente=1)
        self.assertEqual(url, url_autorizacao)

    def test_consulta_cadastro(self):
        url_consulta_cadastro = self.url_base + 'nfe4/services/' \
                                                'CadConsultaCadastro4?wsdl'
        url = localizar_url('NfeConsultaCadastro', '23', ambiente=1)
        self.assertEqual(url, url_consulta_cadastro)

    def test_ret_autorizacao(self):
        url_ret_autorizcao = self.url_base + 'nfe4/services/' \
                                             'NFeRetAutorizacao4?wsdl'
        url = localizar_url('NfeRetAutorizacao', '23', ambiente=1)
        self.assertEqual(url, url_ret_autorizcao)


if __name__ == '__main__':
    unittest.main()
