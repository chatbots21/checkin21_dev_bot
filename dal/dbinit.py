import sqlite3

conn = sqlite3.connect('db.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS participant
			(
				tg_id INTEGER PRIMARY KEY,
				first_name TEXT NOT NULL,
				school_nickname TEXT NOT NULL,
				is_admin INTEGER
			);""")
cur.execute("""CREATE TABLE IF NOT EXISTS event
			(
				event_id INTEGER PRIMARY KEY AUTOINCREMENT,
				short_name CHAR
			);""")
cur.execute("""CREATE TABLE IF NOT EXISTS event_participants
			(
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				event_id INTEGER,
				participant_id INTEGER,
				FOREIGN KEY (event_id)  REFERENCES event (event_id) ON DELETE CASCADE,
				FOREIGN KEY (participant_id)  REFERENCES participant (participant_id) ON DELETE CASCADE
			);""")
conn.commit()