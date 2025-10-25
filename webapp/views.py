"""Flask-AppBuilder views that provide CRUD web interfaces for the models."""

# See https://fontawesome.com/icons for icon names.

import models
from app import appbuilder
from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface


# -------------------------------------------------------------------------------
# Model Views
# -------------------------------------------------------------------------------


class DepartmentModelView(ModelView):
    datamodel = SQLAInterface(models.Department)
    route_base = "/department"
    list_title = "Departments"
    list_columns = ["code", "name", "auh_full_name", "auh_email", "college_code"]


class CollegeModelView(ModelView):
    datamodel = SQLAInterface(models.College)
    route_base = "/college"
    list_title = "Colleges"
    list_columns = ["code", "name", "dean_full_name", "dean_email", "dean_first_name"]
    add_exclude_columns = edit_exclude_columns = show_exclude_columns =["department"]
    related_views = [DepartmentModelView]


class EventModelView(ModelView):
    datamodel = SQLAInterface(models.Event)
    route_base = "/event"
    list_title = "Events"
    list_columns = ["year", "date"]


class FeatureModelView(ModelView):
    datamodel = SQLAInterface(models.Feature)
    route_base = "/feature"
    list_title = "Features"
    list_columns = ["name", "description"]


class RoomModelView(ModelView):
    datamodel = SQLAInterface(models.Room)
    route_base = "/room"
    list_title = "Rooms"
    list_columns = ["name", "type", "capacity", "notes"]


class TimeslotModelView(ModelView):
    datamodel = SQLAInterface(models.Timeslot)
    route_base = "/timeslot"
    list_title = "Timeslots"
    list_columns = ["event_year", "id", "name", "beg_time", "end_time"]
    search_exclude_columns = ["beg_time", "end_time"]


class WorkshopModelView(ModelView):
    datamodel = SQLAInterface(models.Workshop)
    route_base = "/workshop"
    list_title = "Workshops"
    list_columns = [
        "id",
        "state",
        "title",
        "advertisement",
        "description",
        "capacity",
        "computer_needs",
        "room_needs",
        "max_repeat",
        "parent_questions",
        "other_information",
        "event_year",
        "room_name",
    ]


class PersonModelView(ModelView):
    datamodel = SQLAInterface(models.Person)
    route_base = "/person"
    list_title = "Persons"
    list_columns = [
        "email",
        "type",
        "first_name",
        "last_name",
        "phone",
        "department_code",
    ]


class OrganizerModelView(ModelView):
    datamodel = SQLAInterface(models.Organizer)
    route_base = "/organizer"
    list_title = "Organizers"
    list_columns = ["event_year", "person_email", "roles"]


class PersonWorkshopModelView(ModelView):
    datamodel = SQLAInterface(models.PersonWorkshop)
    route_base = "/person_workshop"
    list_title = "Person Workshops"
    list_columns = ["person_email", "workshop_id", "role"]


# -------------------------------------------------------------------------------
# Database Menu
# -------------------------------------------------------------------------------

# appbuilder.add_separator("Admin")


appbuilder.add_view(
    CollegeModelView,
    "Colleges",
    icon="fa-database",
    category="Admin",
    category_icon="fa-database",
)

appbuilder.add_view(
    EventModelView,
    "Events",
    icon="fa-database",
    category="Admin",
)

appbuilder.add_view(
    FeatureModelView,
    "Features",
    icon="fa-database",
    category="Admin",
)

appbuilder.add_view(
    RoomModelView,
    "Rooms",
    icon="fa-database",
    category="Admin",
)

appbuilder.add_view(
    DepartmentModelView,
    "Departments",
    icon="fa-database",
    category="Admin",
)

appbuilder.add_view(
    TimeslotModelView,
    "Time Slots",
    icon="fa-database",
    category="Admin",
)

appbuilder.add_view(
    WorkshopModelView,
    "Workshops",
    icon="fa-database",
    category="Admin",
)

appbuilder.add_view(
    PersonModelView,
    "Persons",
    icon="fa-database",
    category="Admin",
)

appbuilder.add_view(
    OrganizerModelView,
    "Organizers",
    icon="fa-database",
    category="Admin",
)

appbuilder.add_view(
    PersonWorkshopModelView,
    "Person Workshops",
    icon="fa-database",
    category="Admin",
)
