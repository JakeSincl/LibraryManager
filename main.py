from flask import Flask, render_template
#, request, session

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("welcome.html")

app.run(host='0.0.0.0')