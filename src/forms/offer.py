"""
Date:	20/03/2020
Author:	Gerrit Lang


"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class OfferForm(FlaskForm):
    """
    Form for our offer page
    """

    title = StringField("Helper ID", validators=[DataRequired()])
    submit = SubmitField("Get Matches")
