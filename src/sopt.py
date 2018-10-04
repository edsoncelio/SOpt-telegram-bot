# -*- coding: UTF-8 -*-
# configuracoes de chamada a StackAPI
from stackapi import StackAPI
import html
import datetime
import time

#as datas sao usadas em timestamp, precisa converter.
# Ex de entrada: mes-dia-ano
#def timestamp_data(data):
#	return datetime.datetime.fromtimestamp(data)

#inserir no formato: datetime.datetime(2018, 8, 18, 6, 00, 0, 000000)
#def data_timestamp(data):
#	return int(datetime.datetime(2018, 8, 18, 6, 00, 0, 000000)).strftime("%s")

def buscar_questoes(tags):
	#definicao do pt.stackoverflow
	sopt = StackAPI("pt.stackoverflow")

	#conf de numero de resultados
	sopt.page_size = 100
	sopt.max_pages = 1
	resultado = []
	#busca por questoes/tag de acordo com intervalo de tempo(atualmente de 1 dia)
	ts = int(time.time())
	questoes_python = sopt.fetch('questions', min=1, fromdate=ts - 54000, todate=ts)

	for i in range(0, len(questoes_python['items'])):
		for value in tags:
			if value in questoes_python['items'][i]['tags']:
				resultado.append("""
				Titulo: {}
				Link: {}
				Criacao: {}
				""".format(html.unescape(questoes_python['items'][i]['title']),questoes_python['items'][i]['link'],
									questoes_python['items'][i]['creation_date'] ))
	return resultado
