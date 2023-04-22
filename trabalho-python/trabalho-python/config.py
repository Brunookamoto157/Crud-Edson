import os

# Caminho absoluto do diretório do projeto
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Configuração do Flask
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'minha-chave-secreta'  # Altere para uma chave secreta segura
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@hostname/database_name'  # Substitua com suas próprias configurações de banco de dados
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:a1b2c3d4@localhost/banco'  # Substitua com suas próprias configurações de banco de dados


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:a1b2c3d4@localhost/banco'  # Substitua com suas próprias configurações de banco de dados
