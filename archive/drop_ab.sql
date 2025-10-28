-- Drop all tables starting with 'ab_'


SELECT 'DROP TABLE IF EXISTS ' || tablename || ' CASCADE;'
FROM pg_tables
WHERE schemaname = 'public'
  AND tablename LIKE 'ab_%';


DROP TABLE IF EXISTS ab_group CASCADE;
DROP TABLE IF EXISTS ab_group_role CASCADE;
DROP TABLE IF EXISTS ab_permission CASCADE;
DROP TABLE IF EXISTS ab_permission_view CASCADE;
DROP TABLE IF EXISTS ab_permission_view_role CASCADE;
DROP TABLE IF EXISTS ab_register_user CASCADE;
DROP TABLE IF EXISTS ab_role CASCADE;
DROP TABLE IF EXISTS ab_user CASCADE;
DROP TABLE IF EXISTS ab_user_group CASCADE;
DROP TABLE IF EXISTS ab_user_role CASCADE;
DROP TABLE IF EXISTS ab_view_menu CASCADE;
