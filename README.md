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

Algumas credenciais foram removidas do script, pois elas podem dar acesso á API e também ao banco de dados criado na AWS. Para replicar o projeto é necessário atribuir valores as váriaveis relacionadas a credenciais do Banco de Dados, essas são: "database", "user", "password", "host", "port". Para conectar a API é necessário acessar o site "https://developer.spotify.com/" gerar um id e token e passa-los o formato "id:token" na variável auth_string(todas varíaveis presentes no script "spotify_etl.py").

## Inicialização do Airflow

No arquivo "spotify_dag.py" é criado um dicionário chamado "default_args" no qual juntamente com a tupla "dag" serão inicializados valores referentes a orquestração das execuções dos scripts que irão resultar nos processos de ETL agendados. Definido a frequência e inicio das execuções é necessário inicializar o Airflow pelo terminal. Inicialmente deve-se iniciar o banco de dados do airflow com o comando "airflow initdb", isso permitirá que as DAG's sejão armazenadas. Após isso, para ter acesso as DAG's e gerenciá-las o airflow permite a criação de um webserver com o comando: "airflow webserver 4040", o 4040 indica qual porta local será utilizada para iniciar o servidor. Após esses passos serem executados, o comando "airflow scheduler" faz o agendamento e inicia a orquestração.

## Utilizando o QuickSight

O QuickSight é uma ferramenta de visualização de dados, assim como Power BI e Tableau. É possível gerar relatórios nessa ferramenta utilizando a fonte dos dados como planilhas o bancos de dados de diferentes tipos. Nesse projeto, o banco de dados escolhido foi um RDS:Postgre criado na Cloud AWS, o que torna mais fácil toda configuração de Rede e permissões, esse artigo da própria AWS explica como fazer para configurar ambos serviços na mesma rede: "https://docs.aws.amazon.com/quicksight/latest/user/rds-vpc-access.html". Com a VPC configurada é fácil realizar a conexão com o quicksight, basta selecionar o flavour do banco de dados e passar os mesmos valores descritos na etapa de credenciais. Com os dados no banco e a conexão com o QuickSight realizada, torna-se possível a criação de diversos painéis customizados que abrem muitas possibilizades de descobertas e novas ideias.
