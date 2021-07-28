from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):

    name = StringField('Name of Puppy:')
    submit = SubmitField('Add Puppy')


class DelForm(FlaskForm):

    id = IntegerField('Id Number of Puppy to Remove:')
    submit = SubmitField('Remove Puppy')


class AddOwnerForm(FlaskForm):

    name = StringField('Owner Name:')
    puppy_id = IntegerField('Puppy id: ')
    submit = SubmitField('Add Owner')
