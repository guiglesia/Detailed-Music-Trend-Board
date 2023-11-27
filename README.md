# Spotboard: Captação de Dados na Nuvem e Geração de Dashboard para Spotify

Projeto de conclusão do curso de Bacharelado em Sistemas de Informação pela UNICAMP. Esse projeto trata-se da criação de uma pipeline de ETL de dados, utilizando a API do spotfy para gerar visões e insights que a plataforma não dispões. O principla objetivo desse trabalho é a criação de dashboards que atualizam-se com frequência e podem gerar insights significativos para profissionais do ramo da múisica.

Tecnologias utilizadas:
Linguagens: Python, SQL
BD: Postgres
Orquestrador: Airflow
Cloud: AWS
Analytics: Quicksight

## Tecnologias utilizadas

- Linguagens: Python, SQL
- BD: Postgres
- Orquestrador: Airflow
- Cloud: AWS
- Analytics: Quicksight

## Dependências do Projeto

Para que o projeto funcionasse como esperado, foi necessário recorrer à bibliotecas externas, essa bibliotecas possuem métodos que podem ser reútilizados para realizar certas instruções. As dependências para o funcionamento dos scripts estão presentes no diretório root, no arquivo "requirementes.txt", após o clone do repositório basta abrir o terminal e dar o comando "pip3 install -r requirements.txt" no diretório que ele está localizado.

## Instalação e Configuração do AirFlow

O AirFlow torna-se o componente mais complexo à ser configurado para execução e orquestração do processo de ETL. Para que ele funcione e seja instanciado na máquina é preciso que ele seja instalado junto com dependencias relacionadas a versão do python que é desejado utilizar. No projeto, foi utilizado a versão 3.8. Para mais informações a respeito da instalação do AirFlow, todo processo é explicado na documentação oficial no quickstart: https://airflow.apache.org/docs/apache-airflow/stable/start.html

## Credenciais

Algumas credenciais foram removidas do script, pois elas podem dar acesso á api do usuário e também ao banco de dados criado na AWS, para replicar o projeto é necessário passar nos parâmetros os respectivos valores para conectar no Banco de Dados: "database", "user", "password", "host", "port". Para conectar a API é necessário acessar o site "https://developer.spotify.com/" gerar um id e token e passa-los o formato "id:token" na variável auth_string(todas varíaveis presentes no script "spotify_etl.py").
