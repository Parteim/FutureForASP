
class Configuration:
    DEBUG = True
    SECRET_KEY = 'fuck'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1234@localhost/APS'

    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'

    UPLOAD_FOLDER = 'C:/Users/JarAdmin/Desktop/Projects/FutureForASP/src/static/media/'
    ALLOWED_EXTENSIONS = {'pdf', 'docs', 'doc', 'jpg', 'png'}