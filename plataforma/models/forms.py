from flask_wtf import FlaskForm
from wtforms import EmailField ,StringField, DateField, PasswordField, BooleanField, DecimalField
from wtforms.validators import DataRequired
# from wtforms_components import PhoneNumberField

class CadastrarAluno(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    telefone_aluno = StringField('telefone do aluno')
    # telefone_responsavel = PhoneNumberField(country_code = 'BR')

