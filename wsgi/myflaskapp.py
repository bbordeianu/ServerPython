from flask import Flask

from flask import Flask,request, send_from_directory
from flask import render_template
from flask import jsonify
from json import dumps
#from flask.ext.cors import CORS


app = Flask(__name__)
#CORS(app)
global registroAlunni
registroAlunni = {0:{"numeroReg":0,"nome":"ignoto","cognome":"ignoto","annoNascita":"1900"}, 1:{"numeroReg":1,"nome":"ignoto1","cognome":"ignoto1","annoNascita":"1901"}}
positions = {}

@app.route("/")
def hello():
    return render_template( 'index.html')

@app.route("/test")
def test():
    return render_template( 'indexTest.html')

@app.route("/js/<nomeFileJs>")
def jsLoad(nomeFileJs):
    return send_from_directory('js', nomeFileJs)

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

@app.route("/leggiDizionario/", methods = ["POST"])
def leggiDizionario():
    stringa = str(registroAlunni)
    return stringa

@app.route("/insertPosition/", methods = ["POST"])
def insertPosition():
    
    latitude = request.json['latitude']
    longitude = request.json['longitude']
    date = request.json['date']
    
    coordinate = {"latitude" : latitude, "longitude" : longitude}
    
    positions[date] = coordinate
    print positions
    return jsonify("")

@app.route("/readPositions/", methods = ["POST"])
def readPositions():
    stringa = str(positions)
    return stringa

@app.route("/cleanPositions/", methods = ["POST"])
def cleanPositions():
    positions = {}
    return ""
    
if __name__ == "__main__":
    #app.debug=True
    app.run(debug=True, port=5000)
    #65013
