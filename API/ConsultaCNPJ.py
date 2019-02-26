import requests
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'}

def consultar(cnpj):
	url = 'https://www.receitaws.com.br/v1/cnpj/{0}'.format(cnpj)
	req = requests.get(url, headers=headers)
	code = req.status_code
	if code == 200:
		html = req.text
		dados_empresa = json.loads(html)
		return dados_empresa
	else:
		js = { 'status': 'ERROR', 'Valor': 'Error ao Requisitar o Site!' }
		return json.loads(js)
		