import json
import os
import logging
from flask import Flask, request, jsonify
import requests
from pymongo import MongoClient
from encoder import JSONEncoder


#carregando as variáveis do ambiente que estão no arquivo .env
from dotenv import load_dotenv
load_dotenv()

environment = os.getenv('FLASK_ENV')

if environment == 'production':
    from WsgiService import StandaloneApplication

#criando a aplicação flask
app = Flask(__name__)

# Configuração da conexão com o MongoDB
# obtendo a url que está presente no arquivo .env
mongo_uri = f'mongodb://{os.getenv("MONGO_IP")}/'
client = MongoClient(mongo_uri)
db = client['weather']
historico_collection = db['history']

#obtendo a chave da api da versãi 2.5 que está no arquivo .env
api_key = os.getenv('API_KEY') #'eb3f355d27e1b9e73d98a55a7cdef0f9'
url="http://api.openweathermap.org/data/2.5/forecast"

# Rota para obter a previsão do tempo e salvar no histórico
@app.route('/previsao_tempo', methods=['GET'])
def previsao_tempo():    
    #pega o parâmetro da url
    cidade = request.args.get('cidade')
    #validar se o parãmetro de cidade foi fornecido, caso não esteja, retorna um erro
    if not cidade:
        return jsonify({'error': 'Parâmetro "cidade" ausente'}), 400
    
    response = requests.get(url, params={"q": cidade, "exclude":"hourly,alerts,current,minutly", "units":"metric", "appid":api_key})
    if response.status_code == 200:        
        data = response.json()
        # Salva o histórico na coleção      
        historico_collection.insert_one(data)                
        return json.dumps(data, cls=JSONEncoder)
    
    return jsonify({'error': f'Não foi possível obter a previsão do tempo. {response.text}'}), 500

# Rota para consultar o histórico de chamadas
@app.route('/historico', methods=['GET'])
def consultar_historico():
    historico = list(historico_collection.find({}, {}))
    return json.dumps(historico, cls=JSONEncoder)


if __name__ == '__main__':
    try:        
        if environment != 'production':
            logging.info(f'Starting flask develop WSGI on the environment: {environment}')
            app.run(host='0.0.0.0', debug=True, port=os.getenv('OWN_PORT'))
        else:
            logging.info(f'Starting gunicorn on the environment: {environment}')
            gunicornOptions = json.loads(os.getenv('GUNICORN'))
            gunicornOptions.update({"bind": f'0.0.0.0:{os.getenv("OWN_PORT")}'})
            StandaloneApplication(app, gunicornOptions).run()
    except Exception as e:
        logging.error(f'An error has occurred when starting the application: {str(e)}')
