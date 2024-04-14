class Config:
    SECRET_KEY = '1783628bb0b14ce0c636dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://python:password@localhost:5432/plager' #TEMP: Database Credentials for localhost
    SQLALCHEMY_TRACK_MODIFICATIONS = False
