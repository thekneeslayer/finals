class Config:
    SECRET_KEY = "dev-secret-key"
    TESTING = False


class TestConfig(Config):
    TESTING = True
