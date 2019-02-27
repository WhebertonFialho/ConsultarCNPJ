from flask import Flask, jsonify, request, render_template
from flask_bootstrap import Bootstrap
from API import ConsultaCNPJ
import os

app = Flask(__name__, template_folder='templates')
bootstrap = Bootstrap(app)

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/consultar_cnpj/<cnpj>')
def consultar_cnpj(cnpj):
	dados = ConsultaCNPJ.consultar(cnpj)
	if dados['status'] != "ERROR":
		return render_template('dados_empresa.html', data=dados)
	else:
		return render_template('cnpj_invalida.html')

@app.route('/cnpj_invalida')
def cnpj_invalida():
	return render_template('cnpj_invalida.html')
	
if __name__ == '__main__':
	#Bootstrap(app)
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port, debug=True)
