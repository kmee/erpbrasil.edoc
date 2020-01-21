import unittest

from erpbrasil.edoc.nfe import localizar_url


class TesteHomologacaoSantaCatarina(unittest.TestCase):
    url_base = 'https://nfe-homologacao.svrs.rs.gov.br/'

    def test_inutilizacao(self):
        url_inutilizacao = self.url_base + 'ws/nfeinutilizacao/' \
            'nfeinutilizacao4.asmx?wsdl'
        url = localizar_url('NfeInutilizacao', '42')
        self.assertEqual(url, url_inutilizacao)

    def test_consulta_protocolo(self):
        url_consulta_protocolo = self.url_base + 'ws/NfeConsulta/' \
            'NfeConsulta4.asmx?wsdl'
        url = localizar_url('NfeConsultaProtocolo', '42')
        self.assertEqual(url, url_consulta_protocolo)

    def test_status_servico(self):
        url_status_servico = self.url_base + 'ws/NfeStatusServico/' \
            'NfeStatusServico4.asmx?wsdl'
        url = localizar_url('NfeStatusServico', '42')
        self.assertEqual(url, url_status_servico)

    def test_recepcao_evento(self):
        url_recepcao_evento = self.url_base + 'ws/recepcaoevento/' \
            'recepcaoevento4.asmx?wsdl'
        url = localizar_url('RecepcaoEvento', '42')
        self.assertEqual(url, url_recepcao_evento)

    def test_autorizacao(self):
        url_autorizacao = self.url_base + 'ws/NfeAutorizacao/' \
            'NFeAutorizacao4.asmx?wsdl'
        url = localizar_url('NfeAutorizacao', '42')
        self.assertEqual(url, url_autorizacao)

    def test_consulta_cadastro(self):
        url_consulta_cadastro = 'https://cad.svrs.rs.gov.br/ws/' \
                                'cadconsultacadastro/' \
                                'cadconsultacadastro4.asmx?wsdl'
        url = localizar_url('NfeConsultaCadastro', '42')
        self.assertEqual(url, url_consulta_cadastro)

    def test_ret_autorizacao(self):
        url_ret_autorizcao = self.url_base + 'ws/NfeRetAutorizacao/' \
                                             'NFeRetAutorizacao4.asmx?wsdl'
        url = localizar_url('NfeRetAutorizacao', '42')
        self.assertEqual(url, url_ret_autorizcao)


class TesteProducaoSantaCatarina(unittest.TestCase):
    url_base = 'https://nfe.svrs.rs.gov.br/'

    def test_inutilizacao(self):
        url_inutilizacao = self.url_base + 'ws/nfeinutilizacao/' \
                                           'nfeinutilizacao4.asmx?wsdl'
        url = localizar_url('NfeInutilizacao', '42', ambiente=1)
        self.assertEqual(url, url_inutilizacao)

    def test_consulta_protocolo(self):
        url_consulta_protocolo = self.url_base + 'ws/NfeConsulta/' \
                                                 'NfeConsulta4.asmx?wsdl'
        url = localizar_url('NfeConsultaProtocolo', '42', ambiente=1)
        self.assertEqual(url, url_consulta_protocolo)

    def test_status_servico(self):
        url_status_servico = self.url_base + 'ws/NfeStatusServico/' \
                                             'NfeStatusServico4.asmx?wsdl'
        url = localizar_url('NfeStatusServico', '42', ambiente=1)
        self.assertEqual(url, url_status_servico)

    def test_recepcao_evento(self):
        url_recepcao_evento = self.url_base + 'ws/recepcaoevento/' \
                                              'recepcaoevento4.asmx?wsdl'
        url = localizar_url('RecepcaoEvento', '42', ambiente=1)
        self.assertEqual(url, url_recepcao_evento)

    def test_autorizacao(self):
        url_autorizacao = self.url_base + 'ws/NfeAutorizacao/' \
                                          'NFeAutorizacao4.asmx?wsdl'
        url = localizar_url('NfeAutorizacao', '42', ambiente=1)
        self.assertEqual(url, url_autorizacao)

    def test_consulta_cadastro(self):
        url_consulta_cadastro = 'https://cad.svrs.rs.gov.br/ws/' \
                                'cadconsultacadastro/' \
                                'cadconsultacadastro4.asmx?wsdl'
        url = localizar_url('NfeConsultaCadastro', '42', ambiente=1)
        self.assertEqual(url, url_consulta_cadastro)

    def test_ret_autorizacao(self):
        url_ret_autorizcao = self.url_base + 'ws/NfeRetAutorizacao/' \
                                             'NFeRetAutorizacao4.asmx?wsdl'
        url = localizar_url('NfeRetAutorizacao', '42', ambiente=1)
        self.assertEqual(url, url_ret_autorizcao)


if __name__ == '__main__':
    unittest.main()
