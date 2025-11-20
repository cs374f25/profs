"""Forms and FormViews that implement custom features."""

from app import db
from flask import flash, redirect
from flask_appbuilder import PublicFormView, SimpleFormView
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget, Select2Widget
from flask_appbuilder.forms import DynamicForm
from models.tables import Person, PersonWorkshop, Workshop
from wtforms import SelectField, StringField, ValidationError
from wtforms.validators import Email, InputRequired, Length, Regexp


# ------------------------------------------------------------------------------
# Returning Workshop (existing person)
# ------------------------------------------------------------------------------


class ReturningProposerForm(DynamicForm):
    email = StringField(
        ("Email"),
        description=("Enter your email."),
        validators=[InputRequired(), Email()],
        widget=BS3TextFieldWidget(),
    )
    title = StringField(
        ("Workshop name"),
        description=("Enter the workshop name."),
        validators=[InputRequired()],
        widget=BS3TextFieldWidget(),
    )

    def validate_email(self, field):
        """Make sure the email exists when the form is submitted."""
        person = db.session.get(Person, field.data)
        if person is None:
            raise ValidationError("No person with that email exists.")


class ReturningProposerFormView(SimpleFormView):
    form = ReturningProposerForm
    form_title = "Propose a workshop (returning faculty)"

    def form_post(self, form):
        email = form.email.data
        title = form.title.data

        # Create the workshop
        workshop = Workshop(
            state="Proposed",
            title=title,
            event_year=2024,
        )
        db.session.add(workshop)
        db.session.flush()  # Sets workshop.id

        # Create the person_workshop
        link = PersonWorkshop(
            person_email=email,
            workshop_id=workshop.id,
            role="Proposer",
        )
        db.session.add(link)
        db.session.commit()

        # Redirect to the workshop edit form
        flash(f"New workshop {form.title.data} added by {form.email.data}", "info")
        return redirect(f"/workshop/edit/{workshop.id}")


# ------------------------------------------------------------------------------
# New Workshop (create new person)
# ------------------------------------------------------------------------------


class NewProposerForm(DynamicForm):
    email = StringField(
        ("Email"),
        description=("Enter your email."),
        validators=[InputRequired(), Email()],
        widget=BS3TextFieldWidget(),
    )
    first_name = StringField(
        ("First Name"),
        description=("Enter your first name."),
        validators=[InputRequired()],
        widget=BS3TextFieldWidget(),
    )
    last_name = StringField(
        ("Last Name"),
        description=("Enter your last name."),
        validators=[InputRequired()],
        widget=BS3TextFieldWidget(),
    )
    department_code = StringField(
        ("Department Code"),
        description=("Enter your department code."),
        validators=[InputRequired()],
        widget=BS3TextFieldWidget(),
    )
    title = StringField(
        ("Workshop name"),
        description=("Enter the workshop name."),
        validators=[InputRequired()],
        widget=BS3TextFieldWidget(),
    )


class NewProposerFormView(SimpleFormView):
    form = NewProposerForm
    form_title = "Propose a workshop (faculty new to madiSTEM)"

    def form_post(self, form):
        # Create the person
        person = Person(type="Faculty")
        form.populate_obj(person)
        db.session.add(person)

        # Create the workshop
        workshop = Workshop(
            state="Proposed",
            title=form.title.data,
            event_year=2024,
        )
        db.session.add(workshop)
        db.session.flush()  # Sets workshop.id

        # Create the person_workshop
        link = PersonWorkshop(
            person_email=person.email,
            workshop_id=workshop.id,
            role="Proposer",
        )
        db.session.add(link)
        db.session.commit()

        # Redirect to the workshop edit form
        flash(f"New workshop {form.title.data} added by {form.email.data}", "info")
        return redirect(f"/workshop/edit/{workshop.id}")


# ------------------------------------------------------------------------------
# Registration Form (public)
# ------------------------------------------------------------------------------


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
