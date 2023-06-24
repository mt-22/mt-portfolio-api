from dotenv import load_dotenv
import os

load_dotenv()

class ApplicationConfig:
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'mdtaylor.portfolio@gmail.com'
    MAIL_PASSWORD = os.environ['EMAIL_PASS']
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
