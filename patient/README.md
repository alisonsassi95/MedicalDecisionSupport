- README GIT HUB
    

    Link video: https://www.youtube.com/watch?v=e6PkGDH4wWA
    ### Objetivo Geral:
    
    - Desenvolver um modelo computacional que através de variáveis informadas, possa fazer uma listagem por ordem de gravidade dos pacientes que precisam de unidade de tratamento intensivo. Desta forma, facilitar a decisão que o profissional de saúde  recisa tomar na escolha de quem ocupará os leitos.
    
    ### Objetivos Específicos:
    
    - [X]  Extrair os critérios necessários do protocolo AMIB para produção do modelo computacional;
    - [X]  Propor o algoritmo de aprendizado de máquina supervisionado capaz de interpretar
    os critérios;
    - [X]  Codificar a forma de captura dos dados e validação do modelo;
    - [X]  Treinar o algoritmo com os dados dos critérios extraídos;
    - [ ]  Realizar a validação do modelo construído;
    - [ ]  Qualificar a validação reajustando se necessário.
    
    ### Hipótese:
    
    - A tecnologia oferece soluções para problemas complexos, utilizando algoritmos de Inteligencia Artificial, em companhia com a modelagem matemática, é possível criar um modelo computacional baseado no protocolo AMIB 2020 com assertividade e  transparência, conforme critérios predefinidos e treinados, resultando em uma lista de pacientes sugerida pelo modelo desenvolvido, afim de apoiar o profissional da saúde.
    
    ### **MedicalDecisionSupport**:
    
    - É o **nome do sistema** que está sendo desenvolvido para a utilização do Trabalho.


Step by Step Comands

INICIALIZAR AMBIENTE

[] Criar ambiente virtual: 
* Criar um ambiente virtual: python -m venv venv
* Ativar: .\venv\Scripts\activate

[] Rodar comando para as dependências:
* Instalar todos as dependencias: pip install -r requirements.txt

[] Banco de dados:
* Rodar o MakeMigrations: python manage.py makemigrations
* Rodar o Migrate: python manage.py migrate

[] Criar um usuário Admin: python manage.py createsuperuser
Seguir os passos do console.


[] Iniciar servidor:
* Iniciar Servidor: python manage.py runserver

- Comandos
* Gerar o arquivo requeriments: pip freeze > requirements.txt

Comandos inclusos no requirements:
< ------------------------------------->
* Instalar Django: pip install django
* Instalar Models-Utils: pip install django-model-utils
* Instalar Pandas: pip install pandas
* Instalar Scikit: pip install -U scikit-learn
* Instalar Name Fake: pip install Faker
* pip install dj-database-url
<---------------------------------------------->
