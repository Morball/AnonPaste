from flask import Flask 
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
app=Flask(__name__,template_folder="/templates",static_folder="/static")
app.secret_key="32coleslanE"
app.template_folder="templates"
app.static_folder="static"
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["4 per second", "10000 per hour"]
)

from app.views import errors

from app.views import main