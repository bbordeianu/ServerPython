from flask import Flask

#---
import os
from flask import Flask,request, send_from_directory
from flask import render_template
from flask import jsonify
#from flask.ext.cors import CORS

#CORS(app)
#---




app = Flask(__name__)

# simula molto bene un database di dizionari con chiave numerica
# i dizionari possono anche essere vuoti alla partenza
registroAlunni = {0:{"numeroReg":0,"nome":"nome","cognome":"cognome","annoNascita":"1900"}}



@app.route("/")
def hello():
    #DATA_DIR = os.environ.get('OPENSHIFT_DATA_DIR', ".")
    return render_template('index.html')



#---


@app.route("/js/<nomeFilejs>")
def jsLoad():
    return send_from_directory('js', nomeFilejs) 

#---
@app.route("/css/<nomeFileCss>")
def cssLoad(nomeFileCss):
    return send_from_directory('css', nomeFileCss)

@app.route("/insertAlunno/")  # metodo GET per chiamare dalla barra del browser
def inserisciAlunno ():
    # spedizione in formato html
    numeroReg =  request.args.get('numeroReg')
    nome =       request.args.get('nome')
    cognome =    request.args.get('cognome')
    annoNascita =request.args.get('annoNascita') 
    dizAlunno = { "numeroReg": numeroReg, "nome": nome,
                  "cognome" : cognome , "annoNascita":annoNascita}
    registroAlunni[int(numeroReg)]= dizAlunno
    return "OK"   #restituisce status = 200  OK , ma nessuna stringa

@app.route("/alunnoByNumeroReg/", methods=["POST"]) # metodo POST
def alunnoByNumeroReg():
    # spedizione in formato html
    
    numeroReg =  request.json['numeroReg']
    
    dizAlunno = registroAlunni[int(numeroReg)]
    
    #print dizAlunno
    
    # in casi piu' complessi usare render_templates e quindi jsonify
    stringJson = jsonify( ** dizAlunno)
    return stringJson   #aggiunge content-type => json

@app.route("/insertAlunnoPOST/", methods = ["POST"])
def inserisciAlunnoPOST():
    
    numeroReg =     request.json['numeroReg']
    nome =          request.json['nome']
    cognome =       request.json['cognome']
    annoNascita =   request.json['annoNascita']
    
    dizAlunno = {"numeroReg" : numeroReg, "nome" : nome, 
                "cognome" : cognome, "annoNascita"  : annoNascita}
                
    registroAlunni[int(numeroReg)]= dizAlunno
    print dizAlunno
    print registroAlunni[int(numeroReg)]
    return jsonify("")
    
if __name__ == "__main__":
    #app.debug=True
    app.run(debug=True, port=65013)
