from flask import Flask, render_template, redirect, url_for, request
# from flask_login import LoginManager, login_user, current_user, logout_user, login_required
# from flask_hashing import Hashing
# from models import forms
# import bd.aluno as aluno


app = Flask(__name__)
# app.config.from_object('config')

# login_manager = LoginManager()
# login_manager.init_app(app)

# @login_manager.user_loader
# def load_user(_id):
#     return aluno.Aluno(_id)


# @login_manager.unauthorized_handler
# def unauthorized_callback():
#     return redirect(url_for('login_page'))

# hashing = Hashing(app)


# ------------------ PÁGINAS ----------------------

@app.route("/")
def home():
    return 'Olá mundo!'
    return render_template('home.html')
