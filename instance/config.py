TESTCONFIG='jnsjffdj'
MERCHANT_ID = 'HDGFYE123'
DEBUG=True
ADMIN_EMAIL=''
FLASK_RUN_PORT=8080
SECRET_KEY='sjdhbthn'
# JWT_SECRET_KEY = 'secret'

SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://root@localhost/webnews'
SQLALCHEMY_TRACK_MODIFICATIONS=False

SCHEDULER_API_ENABLED=True
SCHEDULER_TIMEZONE='Africa/Lagos'
SCHEDULER_JOB_DEFAULTS = {
    "MAX_INSTANCES": 1,
    "COALESCE": True
}