"""Flask-AppBuilder views that provide CRUD web interfaces for the models."""

# See https://fontawesome.com/icons for icon names.

import models
from app import appbuilder
from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface


# -------------------------------------------------------------------------------
# Database Tables (in same order as drop.sql)
# -------------------------------------------------------------------------------


class PersonWorkshop(ModelView):
    datamodel = SQLAInterface(models.PersonWorkshop)
    route_base = "/person_workshop"
    list_title = "Enrollments"
    list_columns = ["person", "workshop", "role"]


class Workshop(ModelView):
    datamodel = SQLAInterface(models.Workshop)
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
    datamodel = SQLAInterface(models.Timeslot)
    route_base = "/timeslot"
    list_title = "Timeslots"
    list_columns = ["event_year", "id", "name", "beg_time", "end_time"]


class Organizer(ModelView):
    datamodel = SQLAInterface(models.Organizer)
    route_base = "/organizer"
    list_title = "Organizers"
    list_columns = ["event_year", "person_email", "roles"]


class Event(ModelView):
    datamodel = SQLAInterface(models.Event)
    route_base = "/event"
    list_title = "Events"
    list_columns = ["year", "date"]
    add_exclude_columns = edit_exclude_columns = show_exclude_columns = ["organizers", "timeslots", "workshops"]
    related_views = [Organizer, Timeslot, Workshop]


class Person(ModelView):
    datamodel = SQLAInterface(models.Person)
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
    datamodel = SQLAInterface(models.Department)
    route_base = "/department"
    list_title = "Departments"
    list_columns = ["code", "name", "auh_full_name", "auh_email", "college_code"]
    add_exclude_columns = edit_exclude_columns = show_exclude_columns = ["people"]
    related_views = [Person]


class College(ModelView):
    datamodel = SQLAInterface(models.College)
    route_base = "/college"
    list_title = "Colleges"
    list_columns = ["code", "name", "dean_full_name", "dean_email", "dean_first_name"]
    add_exclude_columns = edit_exclude_columns = show_exclude_columns = ["departments"]
    related_views = [Department]


class Room(ModelView):
    datamodel = SQLAInterface(models.Room)
    route_base = "/room"
    list_title = "Rooms"
    list_columns = ["name", "type", "capacity", "notes"]
    add_exclude_columns = edit_exclude_columns = show_exclude_columns = ["workshops"]
    related_views = [Workshop]


class Feature(ModelView):
    datamodel = SQLAInterface(models.Feature)
    route_base = "/feature"
    list_title = "Features"
    list_columns = ["name", "description"]


# -------------------------------------------------------------------------------
# Database Views (in same order as drop.sql)
# -------------------------------------------------------------------------------


class Workshop_Department(ModelView):
    datamodel = SQLAInterface(models.Workshop_Department)
    route_base = '/workshop_department'
    list_title = 'Workshop Leaders'
    list_columns = ['id', 'state', 'title', 'leader', 'first_name', 'last_name', 'department_code', 'college_code']
    base_permissions = ['can_list']


class Workshop_Room(ModelView):
    datamodel = SQLAInterface(models.Workshop_Room)
    route_base = '/workshop_room'
    list_title = 'Workshop Rooms'
    list_columns = ['id', 'state', 'title', 'room_name', 'room_type', 'room_capacity', 'features']
    base_permissions = ['can_list']


class Volunteer_College(ModelView):
    datamodel = SQLAInterface(models.Volunteer_College)
    route_base = '/volunteer_college'
    list_title = 'Volunteers by College'
    list_columns = ['event_year', 'college_code', 'students']
    base_permissions = ['can_list']


class Event_Schedule(ModelView):
    datamodel = SQLAInterface(models.Event_Schedule)
    route_base = '/event_schedule'
    list_title = 'Event Schedules',
    list_columns = ['event_year', 't_id', 'beg_time', 'end_time', 'w_id', 'title', 'advertisement']
    base_permissions = ['can_list']


# -------------------------------------------------------------------------------
# Tables Menu (in an order that makes sense for the GUI)
# -------------------------------------------------------------------------------


appbuilder.add_view(
    College,
    "Colleges",
    icon="fa-database",
    category="Tables",
    category_icon="fa-database",
)

appbuilder.add_view(
    Department,
    "Departments",
    icon="fa-database",
    category="Tables",
)

appbuilder.add_view(
    Person,
    "People",
    icon="fa-database",
    category="Tables",
)

appbuilder.add_view(
    PersonWorkshop,
    "Enrollments",
    icon="fa-database",
    category="Tables",
)

appbuilder.add_separator("Tables")

appbuilder.add_view(
    Workshop,
    "Workshops",
    icon="fa-database",
    category="Tables",
)

appbuilder.add_view(
    Room,
    "Rooms",
    icon="fa-database",
    category="Tables",
)

appbuilder.add_view(
    Feature,
    "Features",
    icon="fa-database",
    category="Tables",
)

appbuilder.add_separator("Tables")

appbuilder.add_view(
    Organizer,
    "Organizers",
    icon="fa-database",
    category="Tables",
)

appbuilder.add_view(
    Event,
    "Events",
    icon="fa-database",
    category="Tables",
)

appbuilder.add_view(
    Timeslot,
    "Time Slots",
    icon="fa-database",
    category="Tables",
)


# -------------------------------------------------------------------------------
# Views Menu (in an order that makes sense for the GUI)
# -------------------------------------------------------------------------------


appbuilder.add_view(
    Event_Schedule,
    "Event Schedules",
    icon="fa-database",
    category="Views",
    category_icon="fa-database",
)

appbuilder.add_view(
    Volunteer_College,
    "Volunteers by College",
    icon="fa-database",
    category="Views",
)

appbuilder.add_view(
    Workshop_Department,
    "Workshop Leaders",
    icon="fa-database",
    category="Views",
)

appbuilder.add_view(
    Workshop_Room,
    "Workshop Rooms",
    icon="fa-database",
    category="Views",
)
