--
-- Workshops by department/college of faculty leader
--
CREATE VIEW workshop_department AS
  SELECT
    id, state, title,
    email AS leader, first_name, last_name,
    department_code, college_code
  FROM workshop
    JOIN person_workshop ON id = workshop_id
    JOIN person ON person_email = email
    JOIN department ON department_code = code
  WHERE role = 'Lead';

--
-- Workshops with assigned room information
--
CREATE VIEW workshop_room AS
  SELECT
    id, state, title,
    name AS room_name, type AS room_type,
    room.capacity AS room_capacity, features
  FROM workshop
    LEFT JOIN room ON room_name = name
    LEFT JOIN (
      SELECT room_name,
        string_agg(feature_name, ', ') AS features
      FROM room_feature
      GROUP BY room_name
    ) USING (room_name);

--
-- Number of student volunteers from each college
--
CREATE VIEW volunteer_college AS
  SELECT event_year, college_code, count(*) AS students
  FROM workshop w
    JOIN person_workshop pw ON id = workshop_id
    JOIN person p ON person_email = email
    JOIN department d ON department_code = d.code
    JOIN college c ON college_code = c.code
  WHERE type = 'Student'
  GROUP BY event_year, college_code;

--
-- Show the detailed schedule of workshops.
--
CREATE VIEW event_schedule AS
  SELECT
    t.event_year, t.id AS t_id, t.beg_time, t.end_time,
    w.id AS w_id, w.title, w.advertisement
  FROM timeslot t
    JOIN workshop_timeslot wt ON t.event_year = wt.timeslot_event_year
                             AND t.id = wt.timeslot_id
   JOIN workshop w ON wt.workshop_id = w.id
  ORDER BY t.id, w.id;
