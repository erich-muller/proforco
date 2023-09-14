from flask import Flask, render_template, redirect, url_for, request
# from flask_login import LoginManager, login_user, current_user, logout_user, login_required
# from flask_hashing import Hashing
# from models import forms
# import bd.aluno as aluno


app = Flask(__name__)
app.config.from_object('config')

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
alunos = {'erich': {'horario': '13:00', 'telefone_aluno': '5522999407306', 'telefone_responsavel': '5522996063008'}}

@app.route("/")
def home():
    return 'Olá mundo!'
    return render_template('home.html')


@app.route("/mensageiro")
def mensageiro():
    # print(alunos)
    return render_template('mensageiro.html', alunos=alunos)


if __name__ == '__main__':
    app.run()