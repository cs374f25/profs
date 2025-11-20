"""Read-only views for showing query results."""

from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from models import queries


# ------------------------------------------------------------------------------
# Database Views (in same order as drop.sql)
# ------------------------------------------------------------------------------


class Workshop_Department(ModelView):
    datamodel = SQLAInterface(queries.Workshop_Department)
    route_base = '/workshop_department'
    list_title = 'Workshop Leaders'
    list_columns = ['id', 'state', 'title', 'leader', 'first_name', 'last_name', 'department_code', 'college_code']
    base_permissions = ['can_list']


class Workshop_Room(ModelView):
    datamodel = SQLAInterface(queries.Workshop_Room)
    route_base = '/workshop_room'
    list_title = 'Workshop Rooms'
    list_columns = ['id', 'state', 'title', 'room_name', 'room_type', 'room_capacity', 'features']
    base_permissions = ['can_list']


class Volunteer_College(ModelView):
    datamodel = SQLAInterface(queries.Volunteer_College)
    route_base = '/volunteer_college'
    list_title = 'Volunteers by College'
    list_columns = ['event_year', 'college_code', 'students']
    base_permissions = ['can_list']


class Event_Schedule(ModelView):
    datamodel = SQLAInterface(queries.Event_Schedule)
    route_base = '/event_schedule'
    list_title = 'Event Schedules',
    list_columns = ['event_year', 't_id', 'beg_time', 'end_time', 'w_id', 'title', 'advertisement']
    base_permissions = ['can_list']
