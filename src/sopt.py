# -*- coding: UTF-8 -*-
# configuracoes de chamada a StackAPI
from stackapi import StackAPI
import html
# import datetime


# as datas sao usadas em timestamp, precisa converter.
# Ex de entrada: mes-dia-ano
# def timestamp_data(data):
#   return datetime.datetime.fromtimestamp(data)

# inserir no formato: datetime.datetime(2018, 8, 18, 6, 00, 0, 000000)
# def data_timestamp(data):
#   return int(datetime.datetime(2018, 8, 18, 6, 00, 0, 000000)).strftime("%s")

def buscar_questoes(tag="python"):
    # definicao do pt.stackoverflow
    sopt = StackAPI("pt.stackoverflow")

    # conf de numero de resultados
    sopt.page_size = 100
    sopt.max_pages = 1
    resultado = []
    # busca por questoes/tag de acordo com intervalo de tempo(atualmente de 1 dia)
    questoes_python = sopt.fetch('questions', min=1, fromdate=1534582800, todate=1534636800, tagged=tag)
    # return str(html.unescape(questoes_python['items'][0]['title']))

    for i in range(0, len(questoes_python['items'])):
        resultado.append("""
        Titulo: {}
        Link: {}
        Criacao: {}
        """.format(html.unescape(questoes_python['items'][i]['title']), questoes_python['items'][i]['link'],
                   questoes_python['items'][i]['creation_date']))
    return resultado
