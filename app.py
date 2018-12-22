from flask import Flask, render_template, flash, redirect, url_for, session, request, make_response
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('search.html')

if __name__ == '__main__':
   app.run(debug = True)
