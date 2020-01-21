import unittest

from erpbrasil.edoc.nfe import localizar_url


class TesteHomologacaoGoias(unittest.TestCase):
    url_base = 'https://homolog.sefaz.go.gov.br/'

    def test_inutilizacao(self):
        url_inutilizacao = self.url_base + 'nfe/services/NFeInutilizacao4?wsdl'
        url = localizar_url('NfeInutilizacao', '52')
        self.assertEqual(url, url_inutilizacao)

    def test_consulta_protocolo(self):
        url_consulta_protocolo = self.url_base + 'nfe/services/' \
                                                 'NFeConsultaProtocolo4?wsdl'
        url = localizar_url('NfeConsultaProtocolo', '52')
        self.assertEqual(url, url_consulta_protocolo)

    def test_status_servico(self):
        url_status_servico = self.url_base + 'nfe/services/' \
                                             'NFeStatusServico4?wsdl'
        url = localizar_url('NfeStatusServico', '52')
        self.assertEqual(url, url_status_servico)

    def test_recepcao_evento(self):
        url_recepcao_evento = self.url_base + 'nfe/services/' \
                                              'NFeRecepcaoEvento4?wsdl'
        url = localizar_url('RecepcaoEvento', '52')
        self.assertEqual(url, url_recepcao_evento)

    def test_autorizacao(self):
        url_autorizacao = self.url_base + 'nfe/services/NFeAutorizacao4?wsdl'
        url = localizar_url('NfeAutorizacao', '52')
        self.assertEqual(url, url_autorizacao)

    def test_consulta_cadastro(self):
        url_consulta_cadastro = self.url_base + 'nfe/services/' \
                                                'CadConsultaCadastro4?wsdl'
        url = localizar_url('NfeConsultaCadastro', '52')
        self.assertEqual(url, url_consulta_cadastro)

    def test_ret_autorizacao(self):
        url_ret_autorizcao = self.url_base + 'nfe/services/' \
                                             'NFeRetAutorizacao4?wsdl'
        url = localizar_url('NfeRetAutorizacao', '52')
        self.assertEqual(url, url_ret_autorizcao)


class TesteProducaoGoias(unittest.TestCase):
    url_base = 'https://nfe.sefaz.go.gov.br/'

    def test_inutilizacao(self):
        url_inutilizacao = self.url_base + 'nfe/services/' \
                                           'NFeInutilizacao4?wsdl'
        url = localizar_url('NfeInutilizacao', '52', ambiente=1)
        self.assertEqual(url, url_inutilizacao)

    def test_consulta_protocolo(self):
        url_consulta_protocolo = self.url_base + 'nfe/services/' \
                                                 'NFeConsultaProtocolo4?wsdl'
        url = localizar_url('NfeConsultaProtocolo', '52', ambiente=1)
        self.assertEqual(url, url_consulta_protocolo)

    def test_status_servico(self):
        url_status_servico = self.url_base + 'nfe/services/' \
                                             'NFeStatusServico4?wsdl'
        url = localizar_url('NfeStatusServico', '52', ambiente=1)
        self.assertEqual(url, url_status_servico)

    def test_recepcao_evento(self):
        url_recepcao_evento = self.url_base + 'nfe/services/' \
                                              'NFeRecepcaoEvento4?wsdl'
        url = localizar_url('RecepcaoEvento', '52', ambiente=1)
        self.assertEqual(url, url_recepcao_evento)

    def test_autorizacao(self):
        url_autorizacao = self.url_base + 'nfe/services/NFeAutorizacao4?wsdl'
        url = localizar_url('NfeAutorizacao', '52', ambiente=1)
        self.assertEqual(url, url_autorizacao)

    def test_consulta_cadastro(self):
        url_consulta_cadastro = self.url_base + 'nfe/services/' \
                                                'CadConsultaCadastro4?wsdl'
        url = localizar_url('NfeConsultaCadastro', '52', ambiente=1)
        self.assertEqual(url, url_consulta_cadastro)

    def test_ret_autorizacao(self):
        url_ret_autorizcao = self.url_base + 'nfe/services/' \
                                             'NFeRetAutorizacao4?wsdl'
        url = localizar_url('NfeRetAutorizacao', '52', ambiente=1)
        self.assertEqual(url, url_ret_autorizcao)


if __name__ == '__main__':
    unittest.main()
