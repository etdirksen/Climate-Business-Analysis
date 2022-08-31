from flask import Flask

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    return 'Hello world, my name is Ethan'

@app.route('/about')
def about_page():
    return "Something."