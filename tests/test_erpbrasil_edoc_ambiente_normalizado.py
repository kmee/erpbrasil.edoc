from types import SimpleNamespace
from unittest import TestCase, skipUnless

from erpbrasil.edoc import cte, mdfe, nfce, nfe
from erpbrasil.edoc.ambiente import em_producao, normalizar_ambiente
from erpbrasil.edoc.provedores import dsf, paulistana
from erpbrasil.edoc.provedores.barueri import Barueri
from erpbrasil.edoc.provedores.dsf import Dsf
from erpbrasil.edoc.provedores.ginfes import Ginfes
from erpbrasil.edoc.provedores.issnet import Issnet
from erpbrasil.edoc.provedores.paulistana import Paulistana

PRODUCAO = (1, "1")
HOMOLOGACAO = (2, "2")
INVALIDOS = (0, 3, "", "0", "3", "producao", None, True, False, 1.0, "1 ")
TRANSMISSAO = SimpleNamespace()
PREFEITURA = (TRANSMISSAO, None, "11", "22")


class TestNormalizacao(TestCase):
    def test_valores_validos(self):
        for valor in PRODUCAO:
            self.assertEqual(normalizar_ambiente(valor), "1")
            self.assertTrue(em_producao(valor))
        for valor in HOMOLOGACAO:
            self.assertEqual(normalizar_ambiente(valor), "2")
            self.assertFalse(em_producao(valor))

    def test_valores_invalidos(self):
        for valor in INVALIDOS:
            with self.assertRaises(ValueError):
                normalizar_ambiente(valor)
            with self.assertRaises(ValueError):
                em_producao(valor)


class TestProcessadoresDFe(TestCase):
    def _processadores(self, ambiente):
        return {
            "nfe": nfe.NFe(TRANSMISSAO, 35, ambiente=ambiente),
            "nfce": nfce.NFCe(TRANSMISSAO, 35, ambiente=ambiente, csc_code="x"),
            "cte": cte.CTe(TRANSMISSAO, 35, ambiente=ambiente),
            "mdfe": mdfe.MDFe(TRANSMISSAO, 35, ambiente=ambiente),
        }

    def test_ambiente_canonico_e_predicado(self):
        for ambiente in PRODUCAO:
            for nome, proc in self._processadores(ambiente).items():
                self.assertEqual(proc.ambiente, "1", nome)
                self.assertTrue(proc.em_producao, nome)
        for ambiente in HOMOLOGACAO:
            for nome, proc in self._processadores(ambiente).items():
                self.assertEqual(proc.ambiente, "2", nome)
                self.assertFalse(proc.em_producao, nome)

    def test_ambiente_invalido_no_construtor(self):
        for valor in INVALIDOS:
            with self.assertRaises(ValueError):
                self._processadores(valor)

    def test_ambiente_invalido_na_atribuicao(self):
        proc = nfe.NFe(TRANSMISSAO, 35)
        with self.assertRaises(ValueError):
            proc.ambiente = 3
        proc.ambiente = 1
        self.assertEqual(proc.ambiente, "1")

    def test_endpoints_nfe_nfce(self):
        for classe in (nfe.NFe, nfce.NFCe):
            prod = classe(TRANSMISSAO, 35, ambiente="1")._get_ws_endpoint(
                nfe.WS_NFE_SITUACAO
            )
            homolog = classe(TRANSMISSAO, 35, ambiente="2")._get_ws_endpoint(
                nfe.WS_NFE_SITUACAO
            )
            self.assertNotEqual(prod, homolog)
            for ambiente in PRODUCAO:
                proc = classe(TRANSMISSAO, 35, ambiente=ambiente)
                self.assertEqual(proc._get_ws_endpoint(nfe.WS_NFE_SITUACAO), prod)
            for ambiente in HOMOLOGACAO:
                proc = classe(TRANSMISSAO, 35, ambiente=ambiente)
                self.assertEqual(proc._get_ws_endpoint(nfe.WS_NFE_SITUACAO), homolog)

    def test_localizar_url_aceita_int_e_texto(self):
        prod = nfe.localizar_url(nfe.WS_NFE_SITUACAO, "35", "55", 1)
        homolog = nfe.localizar_url(nfe.WS_NFE_SITUACAO, "35", "55", 2)
        self.assertNotEqual(prod, homolog)
        self.assertEqual(nfe.localizar_url(nfe.WS_NFE_SITUACAO, "35", "55", "1"), prod)
        self.assertEqual(
            nfe.localizar_url(nfe.WS_NFE_SITUACAO, "35", "55", "2"), homolog
        )
        with self.assertRaises(ValueError):
            nfe.localizar_url(nfe.WS_NFE_SITUACAO, "35", "55", 3)

    def test_nfce_qrcode_e_consulta_por_ambiente(self):
        for ambiente, ambiente_texto in ((1, "1"), ("1", "1"), (2, "2"), ("2", "2")):
            proc = nfce.NFCe(TRANSMISSAO, 35, ambiente=ambiente, csc_code="x")
            sigla = nfce.SIGLA_ESTADO["35"]
            self.assertEqual(
                proc.consulta_qrcode_url,
                nfce.ESTADO_CONSULTA_NFCE[sigla][ambiente_texto],
            )
            self.assertTrue(
                proc.monta_qrcode("1" * 44).startswith(
                    nfce.ESTADO_QRCODE[sigla][ambiente_texto]
                )
            )

    def test_cte_mdfe_get_service_url(self):
        for modulo, servico in (
            (cte, cte.WS_CTE_STATUS_SERVICO),
            (mdfe, mdfe.WS_MDFE_STATUS_SERVICO),
        ):
            prod = modulo.get_service_url("SP", servico, 1)
            homolog = modulo.get_service_url("SP", servico, 2)
            self.assertNotEqual(prod, homolog)
            self.assertEqual(modulo.get_service_url("SP", servico, "1"), prod)
            self.assertEqual(modulo.get_service_url("SP", servico, "2"), homolog)
            with self.assertRaises(ValueError):
                modulo.get_service_url("SP", servico, 3)
            with self.assertRaises(ValueError):
                modulo.get_service_url("SP", servico, None)


class TestProvedoresNFSe(TestCase):
    def test_ginfes(self):
        for ambiente in PRODUCAO:
            proc = Ginfes(TRANSMISSAO, ambiente, 3550308, "11", "22")
            self.assertEqual(proc._url, "https://producao.ginfes.com.br")
            self.assertEqual(proc.ambiente, "1")
        for ambiente in HOMOLOGACAO:
            proc = Ginfes(TRANSMISSAO, ambiente, 3550308, "11", "22")
            self.assertEqual(proc._url, "https://homologacao.ginfes.com.br")
            self.assertEqual(proc.ambiente, "2")

    def test_issnet(self):
        for ambiente in PRODUCAO:
            proc = Issnet(TRANSMISSAO, ambiente, 3543402, "11", "22")
            self.assertNotIn("homologacao", proc._url)
            self.assertTrue(proc.em_producao)
        for ambiente in HOMOLOGACAO:
            proc = Issnet(TRANSMISSAO, ambiente, 3543402, "11", "22")
            self.assertIn("homologacao", proc._url)
            self.assertFalse(proc.em_producao)

    def test_barueri(self):
        for ambiente in PRODUCAO:
            proc = Barueri(TRANSMISSAO, ambiente, 3505708, "11", "22")
            self.assertEqual(proc._url, "https://www.barueri.sp.gov.br/")
        for ambiente in HOMOLOGACAO:
            proc = Barueri(TRANSMISSAO, ambiente, 3505708, "11", "22")
            self.assertEqual(proc._url, "https://testeeiss.barueri.sp.gov.br/")

    def test_paulistana(self):
        for ambiente in PRODUCAO:
            proc = Paulistana(TRANSMISSAO, ambiente, 3550308, "11", "22")
            self.assertIs(proc._servicos, paulistana.servicos_prod)
        for ambiente in HOMOLOGACAO:
            proc = Paulistana(TRANSMISSAO, ambiente, 3550308, "11", "22")
            self.assertIs(proc._servicos, paulistana.servicos_hml)

    @skipUnless(hasattr(dsf, "url"), "nfselib.dsf não instalada")
    def test_dsf(self):
        cidade = next(iter(dsf.url))
        for ambiente in PRODUCAO + HOMOLOGACAO:
            proc = Dsf(TRANSMISSAO, ambiente, cidade, "11", "22")
            self.assertEqual(proc.ambiente, str(ambiente))

    def test_ambiente_invalido(self):
        casos = [
            (Ginfes, 3550308),
            (Issnet, 3543402),
            (Barueri, 3505708),
            (Paulistana, 3550308),
        ]
        if hasattr(dsf, "url"):
            casos.append((Dsf, next(iter(dsf.url))))
        for classe, cidade in casos:
            for valor in INVALIDOS:
                with self.assertRaises(ValueError, msg=f"{classe.__name__} {valor!r}"):
                    classe(TRANSMISSAO, valor, cidade, "11", "22")
