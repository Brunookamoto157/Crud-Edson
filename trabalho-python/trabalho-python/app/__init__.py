from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Cria uma instância do Flask
app = Flask(__name__)

# Configura a aplicação Flask com as configurações definidas em config.py
app.config.from_object('config.DevelopmentConfig')

# Cria uma instância do SQLAlchemy para interagir com o banco de dados
db = SQLAlchemy(app)

# Importa os módulos do aplicativo Flask
from app import views, models