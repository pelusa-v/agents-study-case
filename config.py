class Config:
    SECRET_KEY = ""

class DevelopConfig(Config):
    DEBUG = True

config = {
    'development': DevelopConfig,
}