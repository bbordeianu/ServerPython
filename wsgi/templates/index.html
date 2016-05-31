# -*- coding: utf-8 -*-

from flask import Flask, send_from_directory, request
from json import dumps

registro = { "0": { "nome" : "zero", "cognome" : "negativo", "anno" : "0000"}}

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')

@app.route("/")
def index():
	return send_from_directory("static/", "index.html")

@app.route("/js/<nomeFile>")
def loadJS(nomeFile):
	return send_from_directory("static/js/",nomeFile)

@app.route("/css/<nomeFile>")
def loadCSS(nomeFile):
	return send_from_directory("static/css/",nomeFile)

@app.route("/aggiungiStudente", methods=["POST"])
def aggiungiStudente():
	richiesta = request.get_json(force = True)
	matricola = richiesta["matricola"]
	nome = richiesta["nome"]
	cognome = richiesta["cognome"]
	anno = richiesta["anno"]
	registro[matricola]= {"nome": nome , "cognome": cognome , "anno": anno}
	return dumps ({"success": True}), 200 , {"ContentType": "application/json"}

@app.route("/ottieniStudente", methods=["POST"])
def ottieniStudente():
	richiesta = request.get_json(force = True)
	matricola = richiesta ["matricola"]
	nome = registro [matricola]["nome"]
	cognome = registro [matricola]["cognome"]
	anno = registro [matricola]["anno"]
	return dumps ({"nome": nome, "cognome": cognome, "anno": anno})

if __name__ == "__main__":
	app.run()
