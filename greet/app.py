from flask import Flask
app = Flask(__name__)

@app.route('/welcome')
def return_welcome():
    return 'welcome'

@app.route('/welcome/home')
def return_welcome_home():
    return 'welcome home'

@app.route('/welcome/back')
def return_welcome_back():
    return 'welcome back'



