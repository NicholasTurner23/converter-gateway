from decouple import config as EnvConfig

class Config:
    MONGO_URI = EnvConfig("MONGO_URI")
    AUTH_SVC_ADDRESS = EnvConfig("AUTH_SVC_ADDRESS")