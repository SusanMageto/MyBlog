import os


class Config:
    SECRET_KEY = 'MysecretYoucantryguess'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///myblog.db'  # db url 
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = '' # add os env