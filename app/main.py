from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return render_template("homepage.html")
 
@app.route('/demo')
def experiment():
    return 'Welcome to the demo page'

