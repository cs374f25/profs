"""Flask-AppBuilder views that provide CRUD web interfaces for the models."""

from flask import flash, redirect
from flask_appbuilder import ModelView
from flask_appbuilder.actions import action
from flask_appbuilder.models.sqla.interface import SQLAInterface
from models import tables


# ------------------------------------------------------------------------------
# Database Tables (in same order as drop.sql)
# ------------------------------------------------------------------------------


class PersonWorkshop(ModelView):
    datamodel = SQLAInterface(tables.PersonWorkshop)
    route_base = "/person_workshop"
    list_title = "Enrollments"
    list_columns = ["person", "workshop", "role"]


class Workshop(ModelView):
    datamodel = SQLAInterface(tables.Workshop)
    route_base = "/workshop"
    list_title = "Workshops"
    list_columns = [
        "id",
        "state",
        "title",
        #"advertisement",
        #"description",
        "capacity",
        #"computer_needs",
        #"room_needs",
        #"max_repeat",
        #"parent_questions",
        #"other_information",
        "event_year",
        "room_name",
    ]
    add_exclude_columns = edit_exclude_columns = show_exclude_columns = ["people"]
    related_views = [PersonWorkshop]


class Timeslot(ModelView):
    datamodel = SQLAInterface(tables.Timeslot)
    route_base = "/timeslot"
    list_title = "Timeslots"
    list_columns = ["event_year", "id", "name", "beg_time", "end_time"]


class Organizer(ModelView):
    datamodel = SQLAInterface(tables.Organizer)
    route_base = "/organizer"
    list_title = "Organizers"
    list_columns = ["event_year", "person_email", "roles"]


class Event(ModelView):
    datamodel = SQLAInterface(tables.Event)
    route_base = "/event"
    list_title = "Events"
    list_columns = ["year", "date"]
    add_exclude_columns = edit_exclude_columns = show_exclude_columns = ["organizers", "timeslots", "workshops"]
    related_views = [Organizer, Timeslot, Workshop]


class Person(ModelView):
    datamodel = SQLAInterface(tables.Person)
    route_base = "/person"
    list_title = "People"
    list_columns = [
        "email",
        "type",
        "first_name",
        "last_name",
        "phone",
        "department_code",
    ]
    add_exclude_columns = edit_exclude_columns = show_exclude_columns = ["organizers", "workshops"]
    related_views = [Organizer, PersonWorkshop]


class Department(ModelView):
    datamodel = SQLAInterface(tables.Department)
    route_base = "/department"
    list_title = "Departments"
    list_columns = ["code", "name", "auh_full_name", "auh_email", "college_code"]
    add_exclude_columns = edit_exclude_columns = show_exclude_columns = ["people"]
    related_views = [Person]


class College(ModelView):
    datamodel = SQLAInterface(tables.College)
    route_base = "/college"
    list_title = "Colleges"
    list_columns = ["code", "name", "dean_full_name", "dean_email", "dean_first_name"]
    add_exclude_columns = edit_exclude_columns = show_exclude_columns = ["departments"]
    related_views = [Department]

    @action("myaction", "Send reminder email", "Are you sure?", "fa-email")
    def send_email(self, items):
        # items may be a single College object or a list of College objects
        if not isinstance(items, list):
            items = [items]
        flash(f"{len(items)} emails sent!", "success")
        return redirect(self.get_redirect())


class Room(ModelView):
    datamodel = SQLAInterface(tables.Room)
    route_base = "/room"
    list_title = "Rooms"
    list_columns = ["name", "type", "capacity", "notes"]
    add_exclude_columns = edit_exclude_columns = show_exclude_columns = ["workshops"]
    related_views = [Workshop]


class Feature(ModelView):
    datamodel = SQLAInterface(tables.Feature)
    route_base = "/feature"
    list_title = "Features"
    list_columns = ["name", "description"]
