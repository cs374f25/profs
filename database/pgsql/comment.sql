COMMENT ON TABLE organizer IS 'Tracks the roles of the madiSTEM organizers by year (M-N with event).';

COMMENT ON COLUMN organizer.roles IS 'Comma-separated list of responsibilities';

COMMENT ON TABLE person IS 'The super class entity for all types of people, with their basic information.';

COMMENT ON COLUMN person.email IS 'Use email as the unique identifier for all people';

COMMENT ON COLUMN person.type IS 'Ex: student, faculty, other';

COMMENT ON TABLE department IS 'Needed for name lookups and thank-you emails.';

COMMENT ON COLUMN department.code IS 'Ex: CS';

COMMENT ON TABLE college IS 'Needed for name lookups and thank-you emails.';

COMMENT ON COLUMN college.code IS 'Ex: CISE';

COMMENT ON TABLE event IS 'More attributes to be added later: guest speaker, theme, etc.';

COMMENT ON COLUMN event.year IS 'One event per year';

COMMENT ON COLUMN event.date IS 'The exact date of the event';

COMMENT ON TABLE person_workshop IS 'Connects a person to a workshop with a specific role.';

COMMENT ON COLUMN person_workshop.role IS 'Ex: organizer, volunteer';

COMMENT ON TABLE workshop IS 'Holds all the workshop information.';

COMMENT ON COLUMN workshop.id IS 'Generated auto-increment ID because the title may be edited over time.  This ID is unique across years.';

COMMENT ON COLUMN workshop.state IS 'The state of the workshop -- proposed, accepted, file, etc.  The exact states are not fully defined.';

COMMENT ON COLUMN workshop.advertisement IS 'The workshop description to be shown on the website.';

COMMENT ON COLUMN workshop.description IS 'The full description of the workshop maybe with much more detail than the advertisement.';

COMMENT ON COLUMN workshop.capacity IS 'The max number of students that can be accommodated in this workshop.';

COMMENT ON COLUMN workshop.max_repeat IS 'The number of times this workshop can be offered during the day.';

COMMENT ON COLUMN workshop.parent_questions IS 'Follow-up information/questions for the attendee to share with their parents post event.';

COMMENT ON COLUMN workshop.other_information IS 'Any other information about the workshop to be shared with the organizers.';

COMMENT ON COLUMN workshop.event_year IS 'Not part of the key, but required.';

COMMENT ON COLUMN workshop.room_name IS 'The room is assigned later in the process, so it can be null.';

COMMENT ON TABLE room IS 'Rooms on campus that may be used by madiSTEM.';

COMMENT ON COLUMN room.name IS 'The short name of the room, like King 250';

COMMENT ON COLUMN room.type IS 'Ex: classroom, lab';

COMMENT ON TABLE timeslot IS 'An event is divided into time slots -- these are the schedule for the day.';

COMMENT ON COLUMN timeslot.id IS 'The slots are numbered 1..N from earliest to latest';

COMMENT ON COLUMN timeslot.name IS 'Ex: registration, lunch, speaker, workshops';

COMMENT ON TABLE workshop_timeslot IS 'Connects the workshop to slot M-N, because many workshops can be scheduled in the same slot.';

COMMENT ON TABLE room_feature IS 'M-N connection between room and features (see https://www.lib.jmu.edu/tech-classrooms/).';

COMMENT ON TABLE feature IS 'Just to lookup some features like sink, computers, projector, etc.';
