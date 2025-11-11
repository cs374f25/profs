from flask import flash
from flask_appbuilder import SimpleFormView
from wtforms import BooleanField, StringField, IntegerField, TextAreaField
from wtforms.validators import Email, InputRequired
from flask_appbuilder.forms import DynamicForm
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget

class MyForm(DynamicForm):
    field1 = StringField(('Email'),
        description=('Enter your email.'),
        validators = [InputRequired(), Email()], widget=BS3TextFieldWidget())
    field2 = StringField(('Workshop name'),
        description=('Enter the workshop name.'),
        validators = [InputRequired()], widget=BS3TextFieldWidget())

class MyFormView(SimpleFormView):
    form = MyForm
    form_title = 'Propose a workshop'
    message = 'Workshop entered ... ready to add details'

    def form_get(self, form):
        form.field1.data = 'prefilled'

    def form_post(self, form):
        # post process form
        flash(f'Email: {form.field1.data} Workshop: {form.field2.data}', 'info')
