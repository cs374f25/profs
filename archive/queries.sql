--
-- List workshops organized by the CS department (all years).
--
SELECT Email, FirstName, LastName, Role, Title, Description
FROM department
  JOIN person ON code = department_code
  JOIN person_workshop ON email = person_email
  JOIN workshop ON workshop_id = id
WHERE code = 'CS';

--
-- Get the room information for each workshop in madiSTEM 2024.
--
SELECT w.Title, w.Capacity, r.Building, r.RoomNum, r.Capacity
FROM workshop w
  JOIN room r ON room_id = r.id
WHERE madistem_year = 2024;

--
-- How many volunteers did we have in 2024 from each college?
--
SELECT c.name, count(*) AS volunteers
FROM volunteer v
  JOIN person p ON person_email = email
  JOIN department d ON department_code = d.code
  JOIN college c ON college_code = c.code
WHERE madistem_year = 2024
GROUP BY c.code
ORDER BY volunteers DESC;

--
-- Show the detailed schedule for madiSTEM 2024.
-- TODO We might want to rename the "From" column, since that's a keyword in SQL.
-- TODO We might also want to shorten the column name schedule_slot_madistem_year.
--
SELECT Name, "From", "To", Title, Description
FROM schedule_slot s
  JOIN workshop_in_schedule_slot ON s.id = schedule_slot_id AND s.madistem_year = schedule_slot_madistem_year
  JOIN workshop w ON workshop_id = w.id
WHERE madistem_year = 2024;
