# Como rodar a aplicação?
  ### pré-requisitos
    - Python3.9 <= Python3.10
    - Docker
    - Docker compose
	
  ### Configuraçao environment
	- Configure os dados do arquivo .env (api_key, MONGO_IP, OWN_PORT), sendo:
		-	api_key: é a chave de acesso gerada para acesso a API
		-	MONGO_IP: o IP da maquina onde o Mondo DB esta instalado
		-	OWN_PORT: porta na qual a aplicação ira rodar   
  
  ### Criar um ambiente virtual e instalar as dependências
    - Abra o terminal
    - Navegue para a pasta do projeto
    - Crie o virtualenv com o seguinte comando:
       `python -m venv venv` ou `python3 -m venv venv`
    - Habilite o ambiente virutal com o comando
       No Windows: `venv\Scripts\activate` ou `Script\activate`
       No linux/mac `source bin/activate`
    - Instale os pacotes necessários com o seguinte comando:
      `pip install -r requirements.txt`
    
  ### Rodar a aplicação manualmente via Terminal
	
  ## Opçao 1: utilizando modo debug
  #### Instalar o Mongodb
    - Instale o mongodb utilizando a imagem docker. 
	
	No Windows:

		Certifique-se de que o Docker Desktop esteja instalado e executando.

		Abra o Docker Desktop a partir do menu Iniciar.

		Aguarde até que o Docker esteja totalmente inicializado e em execução.

		Após o Docker estar em execução, execute o comando [docker run] abaixo para iniciar o contêiner MongoDB.

	Rode o seguinte comando:       
       
       `docker run --name some-mongo -p 27017:27017 -d mongo`
       
        Link da imagem docker do mongodb https://hub.docker.com/_/mongo

   - Após fazer os passos anteriores, Navegue para dentro da pasta app
   - execute o comando do python para executar a aplicação:
      `python app.py` ou `python3 app.py`
  
  ## Opçao 2: Rodar aplicação utilizando o docker-compose
    - Builde a imagem docker da aplicação com o seguinte comando:
      `docker build -t weather .` 
    - Navegue terminal para dentro da pasta onde o arquivo docker-compose.yml se encontra
    - Rode o comando abaixo para iniciar as imagens do mongo e da aplicação:
      `docker-compose up -d`

  #### Testar via browser
  
	- Url da previsao
	Substituir o termo NOMEDACIDADE pelo nome da cidade que se deseja testar
	http://192.168.18.8:8000/previsao_tempo?cidade=NOMEDACIDADE
  
	- Url do Historico
	http://192.168.18.8:8000/historico
  
	Nota: substituir o IP conforme IP configurado no arquivo .env

  #### Observações

    - Para rodar a aplicação via docker, foi utilizado o gunicorn. 
	O Gunicorn (Green Unicorn) é um servidor web HTTP para aplicações web escritas em Python para rodar em produção. 
	A função principal do Gunicorn é lidar com solicitações HTTP, fornecendo uma ponte entre o servidor web e a aplicação web Python.
    






