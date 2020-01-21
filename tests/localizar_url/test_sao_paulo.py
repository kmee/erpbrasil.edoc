import unittest

from erpbrasil.edoc.nfe import localizar_url


class TesteHomologacaoSaoPaulo(unittest.TestCase):
    url_base = 'https://homologacao.nfe.fazenda.sp.gov.br/'

    def test_inutilizacao(self):
        url_inutilizacao = self.url_base + 'ws/nfeinutilizacao4.asmx?wsdl'
        url = localizar_url('NfeInutilizacao', '35')
        self.assertEqual(url, url_inutilizacao)

    def test_consulta_protocolo(self):
        url_consulta_protocolo = self.url_base + 'ws/' \
                                                 'nfeconsultaprotocolo4.asmx?wsdl'
        url = localizar_url('NfeConsultaProtocolo', '35')
        self.assertEqual(url, url_consulta_protocolo)

    def test_status_servico(self):
        url_status_servico = self.url_base + 'ws/' \
                                             'nfestatusservico4.asmx?wsdl'
        url = localizar_url('NfeStatusServico', '35')
        self.assertEqual(url, url_status_servico)

    def test_recepcao_evento(self):
        url_recepcao_evento = self.url_base + 'ws/' \
                                              'nferecepcaoevento4.asmx?wsdl'
        url = localizar_url('RecepcaoEvento', '35')
        self.assertEqual(url, url_recepcao_evento)

    def test_autorizacao(self):
        url_autorizacao = self.url_base + 'ws/nfeautorizacao4.asmx?wsdl'
        url = localizar_url('NfeAutorizacao', '35')
        self.assertEqual(url, url_autorizacao)

    def test_consulta_cadastro(self):
        url_consulta_cadastro = self.url_base + 'ws/' \
                                                'cadconsultacadastro4.asmx?wsdl'
        url = localizar_url('NfeConsultaCadastro', '35')
        self.assertEqual(url, url_consulta_cadastro)

    def test_ret_autorizacao(self):
        url_ret_autorizcao = self.url_base + 'ws/' \
                                             'nferetautorizacao4.asmx?wsdl'
        url = localizar_url('NfeRetAutorizacao', '35')
        self.assertEqual(url, url_ret_autorizcao)


class TesteProducaoSaoPaulo(unittest.TestCase):
    url_base = 'https://nfe.fazenda.sp.gov.br/'

    def test_inutilizacao(self):
        url_inutilizacao = self.url_base + 'ws/' \
                                           'nfeinutilizacao4.asmx?wsdl'
        url = localizar_url('NfeInutilizacao', '35', ambiente=1)
        self.assertEqual(url, url_inutilizacao)

    def test_consulta_protocolo(self):
        url_consulta_protocolo = self.url_base + 'ws/' \
                                                 'nfeconsultaprotocolo4.asmx?wsdl'
        url = localizar_url('NfeConsultaProtocolo', '35', ambiente=1)
        self.assertEqual(url, url_consulta_protocolo)

    def test_status_servico(self):
        url_status_servico = self.url_base + 'ws/' \
                                             'nfestatusservico4.asmx?wsdl'
        url = localizar_url('NfeStatusServico', '35', ambiente=1)
        self.assertEqual(url, url_status_servico)

    def test_recepcao_evento(self):
        url_recepcao_evento = self.url_base + 'ws/' \
                                              'nferecepcaoevento4.asmx?wsdl'
        url = localizar_url('RecepcaoEvento', '35', ambiente=1)
        self.assertEqual(url, url_recepcao_evento)

    def test_autorizacao(self):
        url_autorizacao = self.url_base + 'ws/nfeautorizacao4.asmx?wsdl'
        url = localizar_url('NfeAutorizacao', '35', ambiente=1)
        self.assertEqual(url, url_autorizacao)

    def test_consulta_cadastro(self):
        url_consulta_cadastro = self.url_base + 'ws/' \
                                                'cadconsultacadastro4.asmx?wsdl'
        url = localizar_url('NfeConsultaCadastro', '35', ambiente=1)
        self.assertEqual(url, url_consulta_cadastro)

    def test_ret_autorizacao(self):
        url_ret_autorizcao = self.url_base + 'ws/' \
                                             'nferetautorizacao4.asmx?wsdl'
        url = localizar_url('NfeRetAutorizacao', '35', ambiente=1)
        self.assertEqual(url, url_ret_autorizcao)


if __name__ == '__main__':
    unittest.main()
