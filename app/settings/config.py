class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/gestao_estoque.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = Config()