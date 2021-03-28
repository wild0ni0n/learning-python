import flask, flask_login

app = flask.Flask(__name__)
app.secret_key = 'w2eDEi9NcFr4KBXaNKUHZstNLJPPdp5E'

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

# mock user
users  = { 'foo@bar.tld':{ 'password':'secret' }}

class User(flask_login.UserMixin):
    pass

@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return
    user = User()
    user.id = email
    return user

@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return
    user = User()
    user.id = email

@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return
    user = User()
    user.id = email

    user.is_authenticated = request.form['password'] == users[email]['password']
    return user
    