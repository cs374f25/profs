-- Drop all tables and sequences starting with 'ab_'

SELECT 'DROP TABLE IF EXISTS ' || tablename || ' CASCADE;'
FROM pg_tables
WHERE schemaname = 'public'
  AND tablename LIKE 'ab_%'
ORDER BY tablename;

SELECT 'DROP SEQUENCE IF EXISTS ' || sequencename || ' CASCADE;'
FROM pg_sequences
WHERE schemaname = 'public'
  AND sequencename LIKE 'ab_%'
ORDER BY sequencename;

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

DROP SEQUENCE IF EXISTS ab_group_id_seq CASCADE;
DROP SEQUENCE IF EXISTS ab_group_role_id_seq CASCADE;
DROP SEQUENCE IF EXISTS ab_permission_id_seq CASCADE;
DROP SEQUENCE IF EXISTS ab_permission_view_id_seq CASCADE;
DROP SEQUENCE IF EXISTS ab_permission_view_role_id_seq CASCADE;
DROP SEQUENCE IF EXISTS ab_register_user_id_seq CASCADE;
DROP SEQUENCE IF EXISTS ab_role_id_seq CASCADE;
DROP SEQUENCE IF EXISTS ab_user_group_id_seq CASCADE;
DROP SEQUENCE IF EXISTS ab_user_id_seq CASCADE;
DROP SEQUENCE IF EXISTS ab_user_role_id_seq CASCADE;
DROP SEQUENCE IF EXISTS ab_view_menu_id_seq CASCADE;
