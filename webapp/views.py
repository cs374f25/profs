"""Flask-AppBuilder views that provide CRUD web interfaces for the models."""

# See https://fontawesome.com/icons for icon names

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


class FeatureModelView(ModelView):
    datamodel = SQLAInterface(models.Feature)


class RoomModelView(ModelView):
    datamodel = SQLAInterface(models.Room)


class TimeslotModelView(ModelView):
    datamodel = SQLAInterface(models.Timeslot)


class WorkshopModelView(ModelView):
    datamodel = SQLAInterface(models.Workshop)


class PersonModelView(ModelView):
    datamodel = SQLAInterface(models.Person)


class OrganizerModelView(ModelView):
    datamodel = SQLAInterface(models.Organizer)


class PersonWorkshopModelView(ModelView):
    datamodel = SQLAInterface(models.Person)


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
