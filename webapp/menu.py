"""Register all views and build the application menu."""

# See https://fontawesome.com/icons for icon names.


def setup_menu(appbuilder):

    from views import base, charts, forms, queries, tables

    # --------------------------------------------------------------------------
    # Tables Menu (in an order that makes sense for the GUI)
    # --------------------------------------------------------------------------

    appbuilder.add_view(
        tables.College,
        "Colleges",
        icon="fa-database",
        category="Tables",
        category_icon="fa-database",
    )

    appbuilder.add_view(
        tables.Department,
        "Departments",
        icon="fa-database",
        category="Tables",
    )

    appbuilder.add_view(
        tables.Person,
        "People",
        icon="fa-database",
        category="Tables",
    )

    appbuilder.add_view(
        tables.PersonWorkshop,
        "Enrollments",
        icon="fa-database",
        category="Tables",
    )

    appbuilder.add_separator("Tables")

    appbuilder.add_view(
        tables.Workshop,
        "Workshops",
        icon="fa-database",
        category="Tables",
    )

    appbuilder.add_view(
        tables.Room,
        "Rooms",
        icon="fa-database",
        category="Tables",
    )

    appbuilder.add_view(
        tables.Feature,
        "Features",
        icon="fa-database",
        category="Tables",
    )

    appbuilder.add_separator("Tables")

    appbuilder.add_view(
        tables.Organizer,
        "Organizers",
        icon="fa-database",
        category="Tables",
    )

    appbuilder.add_view(
        tables.Event,
        "Events",
        icon="fa-database",
        category="Tables",
    )

    appbuilder.add_view(
        tables.Timeslot,
        "Time Slots",
        icon="fa-database",
        category="Tables",
    )

    # --------------------------------------------------------------------------
    # Views Menu (in an order that makes sense for the GUI)
    # --------------------------------------------------------------------------

    appbuilder.add_view(
        queries.Event_Schedule,
        "Event Schedules",
        icon="fa-database",
        category="Views",
        category_icon="fa-database",
    )

    appbuilder.add_view(
        queries.Volunteer_College,
        "Volunteers by College",
        icon="fa-database",
        category="Views",
    )

    appbuilder.add_view(
        queries.Workshop_Department,
        "Workshop Leaders",
        icon="fa-database",
        category="Views",
    )

    appbuilder.add_view(
        queries.Workshop_Room,
        "Workshop Rooms",
        icon="fa-database",
        category="Views",
    )

    # --------------------------------------------------------------------------
    # Chart Menu (in an order that makes sense for the GUI)
    # --------------------------------------------------------------------------

    appbuilder.add_view(
        charts.Workshop_Department_Chart,
        "Workshop Leaders",
        icon="fa-chart-simple",
        category="Charts",
        category_icon="fa-chart-simple",
    )

    appbuilder.add_view(
        charts.Volunteer_College_Chart,
        "Volunteers by College",
        icon="fa-chart-simple",
        category="Charts",
    )

    # --------------------------------------------------------------------------
    # Custom Views (some might not be in the menu)
    # --------------------------------------------------------------------------

    appbuilder.add_view_no_menu(base.AboutView())

    appbuilder.add_view_no_menu(forms.RegistrationView())

    # --------------------------------------------------------------------------
    # Form Views
    # --------------------------------------------------------------------------

    appbuilder.add_view(
        forms.ReturningProposerFormView,
        "Propose Workshop",
        icon="fa-table-list",
        label="Propose Workshop (returning faculty)",
        category="Forms",
        category_icon="fa-table-list",
    )

    appbuilder.add_view(
       forms.NewProposerFormView,
       "Propose Workshop",
       icon="fa-table-list",
       label='Propose Workshop (new faculty)',
       category="Forms",
       category_icon="fa-table-list")
