# api/index.py

# https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python


from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/about')
def about():
    return 'About!'
