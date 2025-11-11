from flask import flash, redirect, url_for
from flask_appbuilder import SimpleFormView, PublicFormView, expose
from wtforms import BooleanField, StringField, IntegerField, TextAreaField, SelectField
from wtforms.validators import Email, InputRequired, Regexp, Length
from flask_appbuilder.forms import DynamicForm
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget, Select2Widget

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


class RegistrationForm(DynamicForm):
    stu_first = StringField(
        "Student First Name",
        validators=[InputRequired(), Length(max=50)],
        widget=BS3TextFieldWidget(),
    )
    stu_last = StringField(
        "Student Last Name",
        validators=[InputRequired(), Length(max=50)],
        widget=BS3TextFieldWidget(),
    )
    stu_grade = SelectField(
        "Student Grade",
        validators=[InputRequired()],
        choices=[("", ""), ("6", "6th"), ("7", "7th"), ("8", "8th")],
        widget=Select2Widget(),
        default=None,
    )
    stu_school = StringField(
        "School Name",
        validators=[InputRequired(), Length(max=100)],
        widget=BS3TextFieldWidget(),
    )
    stu_zip = StringField(
        "Zip Code",
        validators=[
            InputRequired(),
            Regexp(
                r"^\d{5}(?:-\d{4})?$",
                message="Please enter a valid zip code.",
            ),
        ],
        widget=BS3TextFieldWidget(),
    )
    adult_first = StringField(
        "Adult First Name",
        validators=[InputRequired()],
        widget=BS3TextFieldWidget(),
    )
    adult_last = StringField(
        "Adult Last Name",
        validators=[InputRequired()],
        widget=BS3TextFieldWidget(),
    )
    adult_email = StringField(
        "Adult Email",
        validators=[InputRequired(), Email()],
        widget=BS3TextFieldWidget(),
    )
    adult_phone = StringField(
        "Adult Phone",
        validators=[
            InputRequired(),
            Regexp(
                r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$",
                message="Please enter a valid phone number.",
            ),
        ],
        widget=BS3TextFieldWidget(),
    )


class RegistrationView(PublicFormView):
    route_base = "/register"
    form = RegistrationForm
    form_title = "madiSTEM 2026 Registration Form"

    def form_post(self, form):

        # NOTE we don't yet have a table for participants,
        # but the database update would look something like:
        #
        # registration = Registration()
        # form.populate_obj(registration)
        # db.session.add(registration)
        # db.session.commit()

        flash("Thank you for registering!", "success")
        return redirect(self.get_redirect())
