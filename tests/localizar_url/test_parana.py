import unittest

from erpbrasil.edoc.nfe import localizar_url


class TesteHomologacaoParana(unittest.TestCase):
    url_base = 'https://homologacao.nfe.sefa.pr.gov.br/'

    def test_inutilizacao(self):
        url_inutilizacao = self.url_base + 'nfe/NFeInutilizacao4?wsdl'
        url = localizar_url('NfeInutilizacao', '41')
        self.assertEqual(url, url_inutilizacao)

    def test_consulta_protocolo(self):
        url_consulta_protocolo = self.url_base + 'nfe/' \
                                                 'NFeConsultaProtocolo4?wsdl'
        url = localizar_url('NfeConsultaProtocolo', '41')
        self.assertEqual(url, url_consulta_protocolo)

    def test_status_servico(self):
        url_status_servico = self.url_base + 'nfe/' \
                                             'NFeStatusServico4?wsdl'
        url = localizar_url('NfeStatusServico', '41')
        self.assertEqual(url, url_status_servico)

    def test_recepcao_evento(self):
        url_recepcao_evento = self.url_base + 'nfe/' \
                                              'NFeRecepcaoEvento4?wsdl'
        url = localizar_url('RecepcaoEvento', '41')
        self.assertEqual(url, url_recepcao_evento)

    def test_autorizacao(self):
        url_autorizacao = self.url_base + 'nfe/NFeAutorizacao4?wsdl'
        url = localizar_url('NfeAutorizacao', '41')
        self.assertEqual(url, url_autorizacao)

    def test_consulta_cadastro(self):
        url_consulta_cadastro = self.url_base + 'nfe/' \
                                                'CadConsultaCadastro4?wsdl'
        url = localizar_url('NfeConsultaCadastro', '41')
        self.assertEqual(url, url_consulta_cadastro)

    def test_ret_autorizacao(self):
        url_ret_autorizcao = self.url_base + 'nfe/' \
                                             'NFeRetAutorizacao4?wsdl'
        url = localizar_url('NfeRetAutorizacao', '41')
        self.assertEqual(url, url_ret_autorizcao)


class TesteProducaoParana(unittest.TestCase):
    url_base = 'https://nfe.sefa.pr.gov.br/'

    def test_inutilizacao(self):
        url_inutilizacao = self.url_base + 'nfe/' \
                                           'NFeInutilizacao4?wsdl'
        url = localizar_url('NfeInutilizacao', '41', ambiente=1)
        self.assertEqual(url, url_inutilizacao)

    def test_consulta_protocolo(self):
        url_consulta_protocolo = self.url_base + 'nfe/' \
                                                 'NFeConsultaProtocolo4?wsdl'
        url = localizar_url('NfeConsultaProtocolo', '41', ambiente=1)
        self.assertEqual(url, url_consulta_protocolo)

    def test_status_servico(self):
        url_status_servico = self.url_base + 'nfe/' \
                                             'NFeStatusServico4?wsdl'
        url = localizar_url('NfeStatusServico', '41', ambiente=1)
        self.assertEqual(url, url_status_servico)

    def test_recepcao_evento(self):
        url_recepcao_evento = self.url_base + 'nfe/' \
                                              'NFeRecepcaoEvento4?wsdl'
        url = localizar_url('RecepcaoEvento', '41', ambiente=1)
        self.assertEqual(url, url_recepcao_evento)

    def test_autorizacao(self):
        url_autorizacao = self.url_base + 'nfe/NFeAutorizacao4?wsdl'
        url = localizar_url('NfeAutorizacao', '41', ambiente=1)
        self.assertEqual(url, url_autorizacao)

    def test_consulta_cadastro(self):
        url_consulta_cadastro = self.url_base + 'nfe/' \
                                                'CadConsultaCadastro4?wsdl'
        url = localizar_url('NfeConsultaCadastro', '41', ambiente=1)
        self.assertEqual(url, url_consulta_cadastro)

    def test_ret_autorizacao(self):
        url_ret_autorizcao = self.url_base + 'nfe/' \
                                             'NFeRetAutorizacao4?wsdl'
        url = localizar_url('NfeRetAutorizacao', '41', ambiente=1)
        self.assertEqual(url, url_ret_autorizcao)


if __name__ == '__main__':
    unittest.main()
