from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, HiddenField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, Length, ValidationError



class FormConsulta(FlaskForm):
    id = HiddenField('id')
    from_currency = SelectMultipleField(choices=[('EUR'), ('USD'), ('BTC')]) #)('Inicial Currency', [validators.required()])) #=[DataRequired(), Length(min=3, message="Three characters at least")])
    #precio_unitario = FloatField('Precio U.', validators=[DataRequired(message="Introduce algo, nano")])
    #coste_unitario = FloatField('Coste U.', validators=[DataRequired(), valida_coste])

    submit = SubmitField('Aceptar')


'''
    https://pro-api.coinmarketcap.com/v1/tools/price-conversion?amount=1&symbol=<From>&convert=<To>CMC_PRO_API_KEY=<vuestra_api_key>

    <lista monedas>    <lista monedas destino>

    <cantidad>      <Precio Unitario>

                        <Precio total>

                        Boton Boton
'''
