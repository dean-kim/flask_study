from flask import Flask, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def index(): pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
    else:
        error = 'Inavalid username/password'
    return render_template('login.html', error=error)

@app.route('/user/<username>')
def profile(username): pass

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='Dean Kim'))