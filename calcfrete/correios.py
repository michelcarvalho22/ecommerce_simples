import requests
import json
from django.conf import settings
from  bs4 import BeautifulSoup
import urllib.parse
import urllib.request
from xml.dom import minidom
import re




class Correios(object):

    PAC = '04510'
    SEDEX = '40010'
    SEDEX_10 = '40215'
    SEDEX_HOJE = '40290'
    E_SEDEX = '81019'
    OTE = '44105'
    NORMAL = '41017'
    SEDEX_A_COBRAR = '40045'

    def __init__(self):
        self.status = 'OK'

    def _getDados(self, tags_name, dom):
        dados = {}

        for tag_name in tags_name:
            try:
                dados[tag_name] = dom.getElementsByTagName(tag_name)[0]
                dados[tag_name] = dados[tag_name].childNodes[0].data
            except:
                dados[tag_name] = ''

        return dados

    # Vários campos viraram obrigatórios para cálculo de frete:
    # http://www.correios.com.br/webServices/PDF/SCPP_manual_implementacao_calculo_remoto_de_precos_e_prazos.pdf (páginas 2 e 3)
    def frete(self, cod, GOCEP, HERECEP, peso, formato,
              comprimento, altura, largura, diametro, mao_propria='N',
              valor_declarado='0', aviso_recebimento='N',
              empresa='', senha='', toback='xml'):

        base_url = "http://ws.correios.com.br/calculador/CalcPrecoPrazo.aspx"

        fields = [
            ('nCdEmpresa', empresa),
            ('sDsSenha', senha),
            ('nCdServico', cod),
            ('sCepOrigem', HERECEP),
            ('sCepDestino', GOCEP),
            ('nVlPeso', peso),
            ('nCdFormato', formato),
            ('nVlComprimento', comprimento),
            ('nVlAltura', altura),
            ('nVlLargura', largura),
            ('nVlDiametro', diametro),
            ('sCdMaoPropria', mao_propria),
            ('nVlValorDeclarado', valor_declarado),
            ('sCdAvisoRecebimento', aviso_recebimento),
            ('StrRetorno', toback),
        ]

        url = base_url + "?" + urllib.parse.urlencode(fields)
        dom = minidom.parse(urllib.request.urlopen(url))

        tags_name = ('MsgErro',
                     'Erro',
                     'Codigo',
                     'Valor',
                     'PrazoEntrega',
                     'ValorMaoPropria',
                     'ValorValorDeclarado',
                     'EntregaDomiciliar',
                     'EntregaSabado',)

        return self._getDados(tags_name, dom)


