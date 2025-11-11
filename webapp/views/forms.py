from flask import flash, redirect
from flask_appbuilder import SimpleFormView
from wtforms import BooleanField, StringField, IntegerField, TextAreaField
from wtforms.validators import Email, InputRequired
from flask_appbuilder.forms import DynamicForm
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget

import psycopg
import socket

try:
    socket.gethostbyname("data.cs.jmu.edu")
    DSN = "host=data.cs.jmu.edu user=profs dbname=profs"
except:
    DSN = "host=localhost user=profs dbname=profs"


def new_proposer_workshop(email, title):
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            cur.execute("""INSERT INTO person (email, type, first_name, last_name, department_code )
                        VALUES (%s, 'Faculty', 'first', 'last', 'CS')""",
                        (email,))
            cur.execute("INSERT INTO workshop (state, title, event_year) values ('Proposed', %s, 2024)", (title,))
            cur.execute("INSERT INTO person_workshop (person_email, workshop_id, role) values (%s, lastval(), 'Proposer')", (email,))
            cur.execute("SELECT lastval()")
            conn.commit()
            return cur.fetchone()

def returning_proposer_workshop(email, title):
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            # this is a faculty member who is in the database already
            cur.execute("INSERT INTO workshop (state, title, event_year) values ('Proposed', %s, 2024)", (title,))
            cur.execute("INSERT INTO person_workshop (person_email, workshop_id, role) values (%s, lastval(), 'Proposer')", (email,))
            cur.execute("SELECT lastval()")
            conn.commit()
            return cur.fetchone()

class ReturningProposerForm(DynamicForm):
    field1 = StringField(('Email'),
        description=('Enter your email.'),
        validators = [InputRequired(), Email()], widget=BS3TextFieldWidget())
    field2 = StringField(('Workshop name'),
        description=('Enter the workshop name.'),
        validators = [InputRequired()], widget=BS3TextFieldWidget())

class ReturningFormView(SimpleFormView):
    form = ReturningProposerForm
    form_title = 'Propose a workshop (returning faculty)'

    # def form_get(self, form):
    #     form.field1.data = 'prefilled'

    def form_post(self, form):
        # post process form
        id = returning_proposer_workshop(form.field1.data, form.field2.data)
        flash(f'New workshop {form.field2.data} added by {form.field1.data}', 'info')
        return redirect(f"/workshop/edit/{id[0]}")
