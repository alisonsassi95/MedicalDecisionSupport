- README GIT HUB
    
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

* Criar um ambiente virtual: python -m venv venv

* Ativar: .\venv\Scripts\activate

* Instalar Django: pip install django
* Instalar Models-Utils: pip install django-model-utils

* Instalar Pandas: pip install pandas

* Instalar Scikit: pip install -U scikit-learn

Rodar o MakeMigrations:python manage.py makemigrations
Rodar o Migrate: python manage.py migrate

* Instalar todos os plugins: pip install -r requirements.txt

* Iniciar Servidor: python manage.py runserver


Adicione esses comandos abaixo nesse arquivo: "requirements.txt" e salve na raiz ( na mesma pasta do README)
Começa aqui:

arabic-reshaper==2.1.3
argon2-cffi==21.1.0
asgiref==3.4.1
attrs==21.2.0
backcall==0.2.0
bleach==4.1.0
certifi==2021.5.30
cffi==1.15.0
chardet==4.0.0
colorama==0.4.4
debugpy==1.5.1
decorator==5.1.0
defusedxml==0.7.1
Django==3.2.5
django-js-asset==1.2.2
download==0.3.5
entrypoints==0.3
future==0.18.2
idna==2.10
ipykernel==6.5.0
ipython==7.29.0
ipython-genutils==0.2.0
jedi==0.18.0
Jinja2==3.0.2
jsonschema==4.2.1
jupyter-client==7.0.6
jupyter-core==4.9.1
jupyterlab-pygments==0.1.2
MarkupSafe==2.0.1
matplotlib-inline==0.1.3
mistune==0.8.4
mysqlclient==2.0.3
nbclient==0.5.5
nbconvert==6.2.0
nbformat==5.1.3
nest-asyncio==1.5.1
notebook==6.4.5
numpy==1.21.4
packaging==21.2
pandas==1.3.4
pandocfilters==1.5.0
parso==0.8.2
pickleshare==0.7.5
Pillow==8.3.0
prometheus-client==0.12.0
prompt-toolkit==3.0.22
pycparser==2.21
Pygments==2.10.0
pyparsing==2.4.7
PyPDF2==1.26.0
pyrsistent==0.18.0
python-bidi==0.4.2
python-dateutil==2.8.2
pytz==2021.1
pywin32==302
pywinpty==1.1.5
pyxml2pdf==0.3.0
pyzmq==22.3.0
reportlab==3.5.68
requests==2.25.1
scikit-learn==1.0.1
scipy==1.7.2
Send2Trash==1.8.0
six==1.16.0
sklearn==0.0
sqlparse==0.4.1
terminado==0.12.1
testpath==0.5.0
threadpoolctl==3.0.0
tornado==6.1
tqdm==4.61.1
traitlets==5.1.1
urllib3==1.26.6
wcwidth==0.2.5
webencodings==0.5.1


Terminou o arquivo, agora só rodar o comando.

