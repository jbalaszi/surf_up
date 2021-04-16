# Import dependencies
from flask import Flask

#Create new Flask instance
app = Flask(__name__)

# Create first route
@app.route('/')
def hello_world():
    return 'Hello world'