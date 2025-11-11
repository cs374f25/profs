from flask import flash, redirect, url_for
from flask_appbuilder import SimpleFormView, PublicFormView, expose
from wtforms import BooleanField, StringField, IntegerField, TextAreaField, SelectField
from wtforms.validators import Email, InputRequired, Regexp, Length
from flask_appbuilder.forms import DynamicForm
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget, Select2Widget

import psycopg
import socket

try:
    socket.gethostbyname("data.cs.jmu.edu")
    DSN = "host=data.cs.jmu.edu user=profs dbname=profs"
except:
    DSN = "host=localhost user=profs dbname=profs"


# ProposeWorkshop Database functions

def new_proposer_workshop(email, first, last, dept_code, title):
   with psycopg.connect(DSN) as conn:
       with conn.cursor() as cur:
           cur.execute("""INSERT INTO person (email, type, first_name, last_name, department_code )
                       VALUES (%s, 'Faculty', %s, %s, %s)""",
                       (email, first, last, dept_code))
           cur.execute("INSERT INTO workshop (state, title, event_year) values ('Proposed', %s, 2024)", (title,))
           cur.execute("INSERT INTO person_workshop (person_email, workshop_id, role) values (%s, lastval(), 'Proposer')", (email,))
           cur.execute("SELECT lastval()")
           conn.commit()
           return cur.fetchone()[0]


def returning_proposer_workshop(email, title):
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            # this is a faculty member who is in the database already
            cur.execute("INSERT INTO workshop (state, title, event_year) values ('Proposed', %s, 2024)", (title,))
            cur.execute("INSERT INTO person_workshop (person_email, workshop_id, role) values (%s, lastval(), 'Proposer')", (email,))
            cur.execute("SELECT lastval()")
            conn.commit()
            return cur.fetchone()[0]

# ProposeWorkshop Forms

class ReturningProposerForm(DynamicForm):
    field1 = StringField(('Email'),
        description=('Enter your email.'),
        validators = [InputRequired(), Email()], widget=BS3TextFieldWidget())
    field2 = StringField(('Workshop name'),
        description=('Enter the workshop name.'),
        validators = [InputRequired()], widget=BS3TextFieldWidget())

class NewProposerForm(DynamicForm):
   f_email = StringField(('Email'),
       description=('Enter your email.'),
       validators = [InputRequired(), Email()], widget=BS3TextFieldWidget())
   f_first = StringField(('First Name'),
       description=('Enter your first name.'),
       validators = [InputRequired()], widget=BS3TextFieldWidget())
   f_last = StringField(('Last Name'),
       description=('Enter your last name.'),
       validators = [InputRequired()], widget=BS3TextFieldWidget())
   f_dept = StringField(('Department Code'),
       description=('Enter your department code.'),
       validators = [InputRequired()], widget=BS3TextFieldWidget())
   f_wkshop = StringField(('Workshop name'),
       description=('Enter the workshop name.'),
       validators = [InputRequired()], widget=BS3TextFieldWidget())

# ProposeWorkshop FormViews

class ReturningProposerFormView(SimpleFormView):
    form = ReturningProposerForm
    form_title = 'Propose a workshop (returning faculty)'

    # def form_get(self, form):
    #     form.field1.data = 'prefilled'

    def form_post(self, form):
        # post process form
        id = returning_proposer_workshop(form.field1.data, form.field2.data)
        flash(f'New workshop {form.field2.data} added by {form.field1.data}', 'info')
        return redirect(f"/workshop/edit/{id}")

class NewProposerFormView(SimpleFormView):
   form = NewProposerForm
   form_title = 'Propose a workshop (faculty new to madiSTEM)'

   def form_post(self, form):
       # post process form
       id = new_proposer_workshop(form.f_email.data, form.f_first.data, form.f_last.data, form.f_dept.data, form.f_wkshop.data)
       flash(f'New workshop {form.f_wkshop.data} added by {form.f_email.data}', 'info')
       return redirect(f"/workshop/edit/{id}")

# Registration Form

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
