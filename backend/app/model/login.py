from flask_bcrypt import Bcrypt
from flask_httpauth import HTTPBasicAuth

app_bcrypt = Bcrypt()
app_auth = HTTPBasicAuth()