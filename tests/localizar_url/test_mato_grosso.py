import unittest

from erpbrasil.edoc.nfe import localizar_url


class TesteHomologacaoMatoGrosso(unittest.TestCase):
    url_base = 'https://homologacao.sefaz.mt.gov.br/'

    def test_inutilizacao(self):
        url_inutilizacao = self.url_base + 'nfews/v2/services/' \
                                           'NfeInutilizacao4?wsdl'
        url = localizar_url('NfeInutilizacao', '51')
        self.assertEqual(url, url_inutilizacao)

    def test_consulta_protocolo(self):
        url_consulta_protocolo = self.url_base + 'nfews/v2/services/' \
                                                 'NfeConsulta4?wsdl'
        url = localizar_url('NfeConsultaProtocolo', '51')
        self.assertEqual(url, url_consulta_protocolo)

    def test_status_servico(self):
        url_status_servico = self.url_base + 'nfews/v2/services/' \
                                             'NfeStatusServico4?wsdl'
        url = localizar_url('NfeStatusServico', '51')
        self.assertEqual(url, url_status_servico)

    def test_recepcao_evento(self):
        url_recepcao_evento = self.url_base + 'nfews/v2/services/' \
                                              'RecepcaoEvento4?wsdl'
        url = localizar_url('RecepcaoEvento', '51')
        self.assertEqual(url, url_recepcao_evento)

    def test_autorizacao(self):
        url_autorizacao = self.url_base + 'nfews/v2/services/' \
                                          'NfeAutorizacao4?wsdl'
        url = localizar_url('NfeAutorizacao', '51')
        self.assertEqual(url, url_autorizacao)

    def test_consulta_cadastro(self):
        url_consulta_cadastro = self.url_base + 'nfews/v2/services/' \
                                                'CadConsultaCadastro4?wsdl'
        url = localizar_url('NfeConsultaCadastro', '51')
        self.assertEqual(url, url_consulta_cadastro)

    def test_ret_autorizacao(self):
        url_ret_autorizcao = self.url_base + 'nfews/v2/services/' \
                                             'NfeRetAutorizacao4?wsdl'
        url = localizar_url('NfeRetAutorizacao', '51')
        self.assertEqual(url, url_ret_autorizcao)


class TesteProducaoMatoGrosso(unittest.TestCase):
    url_base = 'https://nfe.sefaz.mt.gov.br/'

    def test_inutilizacao(self):
        url_inutilizacao = self.url_base + 'nfews/v2/services/' \
                                           'NfeInutilizacao4?wsdl'
        url = localizar_url('NfeInutilizacao', '51', ambiente=1)
        self.assertEqual(url, url_inutilizacao)

    def test_consulta_protocolo(self):
        url_consulta_protocolo = self.url_base + 'nfews/v2/services/' \
                                                 'NfeConsulta4?wsdl'
        url = localizar_url('NfeConsultaProtocolo', '51', ambiente=1)
        self.assertEqual(url, url_consulta_protocolo)

    def test_status_servico(self):
        url_status_servico = self.url_base + 'nfews/v2/services/' \
                                             'NfeStatusServico4?wsdl'
        url = localizar_url('NfeStatusServico', '51', ambiente=1)
        self.assertEqual(url, url_status_servico)

    def test_recepcao_evento(self):
        url_recepcao_evento = self.url_base + 'nfews/v2/services/' \
                                              'RecepcaoEvento4?wsdl'
        url = localizar_url('RecepcaoEvento', '51', ambiente=1)
        self.assertEqual(url, url_recepcao_evento)

    def test_autorizacao(self):
        url_autorizacao = self.url_base + 'nfews/v2/services/' \
                                          'NfeAutorizacao4?wsdl'
        url = localizar_url('NfeAutorizacao', '51', ambiente=1)
        self.assertEqual(url, url_autorizacao)

    def test_consulta_cadastro(self):
        url_consulta_cadastro = self.url_base + 'nfews/v2/services/' \
                                                'CadConsultaCadastro4?wsdl'
        url = localizar_url('NfeConsultaCadastro', '51', ambiente=1)
        self.assertEqual(url, url_consulta_cadastro)

    def test_ret_autorizacao(self):
        url_ret_autorizcao = self.url_base + 'nfews/v2/services/' \
                                             'NfeRetAutorizacao4?wsdl'
        url = localizar_url('NfeRetAutorizacao', '51', ambiente=1)
        self.assertEqual(url, url_ret_autorizcao)


if __name__ == '__main__':
    unittest.main()
