import unittest

from erpbrasil.edoc.nfe import localizar_url


class TesteHomologacaoMatoGrossoSul(unittest.TestCase):
    url_base = 'https://hom.nfe.sefaz.ms.gov.br/'

    def test_inutilizacao(self):
        url_inutilizacao = self.url_base + 'ws/NFeInutilizacao4?wsdl'
        url = localizar_url('NfeInutilizacao', '50')
        self.assertEqual(url, url_inutilizacao)

    def test_consulta_protocolo(self):
        url_consulta_protocolo = self.url_base + 'ws/' \
                                                 'NFeConsultaProtocolo4?wsdl'
        url = localizar_url('NfeConsultaProtocolo', '50')
        self.assertEqual(url, url_consulta_protocolo)

    def test_status_servico(self):
        url_status_servico = self.url_base + 'ws/' \
                                             'NFeStatusServico4?wsdl'
        url = localizar_url('NfeStatusServico', '50')
        self.assertEqual(url, url_status_servico)

    def test_recepcao_evento(self):
        url_recepcao_evento = self.url_base + 'ws/' \
                                              'NFeRecepcaoEvento4?wsdl'
        url = localizar_url('RecepcaoEvento', '50')
        self.assertEqual(url, url_recepcao_evento)

    def test_autorizacao(self):
        url_autorizacao = self.url_base + 'ws/NFeAutorizacao4?wsdl'
        url = localizar_url('NfeAutorizacao', '50')
        self.assertEqual(url, url_autorizacao)

    def test_consulta_cadastro(self):
        url_consulta_cadastro = self.url_base + 'ws/' \
                                                'CadConsultaCadastro4?wsdl'
        url = localizar_url('NfeConsultaCadastro', '50')
        self.assertEqual(url, url_consulta_cadastro)

    def test_ret_autorizacao(self):
        url_ret_autorizcao = self.url_base + 'ws/' \
                                             'NFeRetAutorizacao4?wsdl'
        url = localizar_url('NfeRetAutorizacao', '50')
        self.assertEqual(url, url_ret_autorizcao)


class TesteProducaoMatoGrossoSul(unittest.TestCase):
    url_base = 'https://nfe.sefaz.ms.gov.br/'

    def test_inutilizacao(self):
        url_inutilizacao = self.url_base + 'ws/' \
                                           'NFeInutilizacao4?wsdl'
        url = localizar_url('NfeInutilizacao', '50', ambiente=1)
        self.assertEqual(url, url_inutilizacao)

    def test_consulta_protocolo(self):
        url_consulta_protocolo = self.url_base + 'ws/' \
                                                 'NFeConsultaProtocolo4?wsdl'
        url = localizar_url('NfeConsultaProtocolo', '50', ambiente=1)
        self.assertEqual(url, url_consulta_protocolo)

    def test_status_servico(self):
        url_status_servico = self.url_base + 'ws/' \
                                             'NFeStatusServico4?wsdl'
        url = localizar_url('NfeStatusServico', '50', ambiente=1)
        self.assertEqual(url, url_status_servico)

    def test_recepcao_evento(self):
        url_recepcao_evento = self.url_base + 'ws/' \
                                              'NFeRecepcaoEvento4?wsdl'
        url = localizar_url('RecepcaoEvento', '50', ambiente=1)
        self.assertEqual(url, url_recepcao_evento)

    def test_autorizacao(self):
        url_autorizacao = self.url_base + 'ws/NFeAutorizacao4?wsdl'
        url = localizar_url('NfeAutorizacao', '50', ambiente=1)
        self.assertEqual(url, url_autorizacao)

    def test_consulta_cadastro(self):
        url_consulta_cadastro = self.url_base + 'ws/' \
                                                'CadConsultaCadastro4?wsdl'
        url = localizar_url('NfeConsultaCadastro', '50', ambiente=1)
        self.assertEqual(url, url_consulta_cadastro)

    def test_ret_autorizacao(self):
        url_ret_autorizcao = self.url_base + 'ws/' \
                                             'NFeRetAutorizacao4?wsdl'
        url = localizar_url('NfeRetAutorizacao', '50', ambiente=1)
        self.assertEqual(url, url_ret_autorizcao)


if __name__ == '__main__':
    unittest.main()
