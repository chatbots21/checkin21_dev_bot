PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
create table event(id int, short_name varchar, description varchar, date_start varchar, date_end varchar);
create table event_participant(id int, event_id int, participant_id int);
create table participant(id int, tg_id int, school_nickname varchar, first_name varchar);
COMMIT;

